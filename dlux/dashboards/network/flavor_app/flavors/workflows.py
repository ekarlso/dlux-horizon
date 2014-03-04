# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Endre Karlson <endre.karlson@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import logging

from django.utils.translation import ugettext_lazy as _
from horizon import forms
from horizon import workflows

from dlux import api

LOG = logging.getLogger(__name__)


class SetFlavorDetailsAction(workflows.Action):
    name = forms.CharField(max_length=50, label=_('Flavor Name'))
    description = forms.CharField(max_length=140, label=('Description'))
    fwd_class = forms.ChoiceField(label=_('Class'))

    def populate_fwd_class_choices(self, request, context):
        choices = []
        client = api.get_client(request)
        try:
            classes = client.flavor_app.classes.list()
            for c in classes:
                tmp = (c.id, c.name)
                choices.append(tmp)

        except Exception:
            return choices

        self.fields['fwd_class'].choices = choices
        return choices

    class Meta:
        name = _('Details')


class SetFlavorDetails(workflows.Step):
    action_class = SetFlavorDetailsAction
    contributes = ['name', 'description', 'fwd_class']


class CreateFlavor(workflows.Workflow):
    slug = 'create_flavor'
    name = _("Create Flavor")
    finalize_button_name = _("Create")
    success_message = _('Created flavor')
    failure_message = _('Unable to add Flavor.')
    success_url = "horizon:network:flavor_app:index"
    default_steps = (SetFlavorDetails,)

    def handle(self, request, context):
        client = api.get_client(request)
        try:
            client.flavor_app.flavors.create(**context)
            return True
        except Exception:
            return False
