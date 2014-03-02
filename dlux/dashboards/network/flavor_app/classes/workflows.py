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


class SetClassDetailsAction(workflows.Action):
    name = forms.CharField(max_length=100, label=_('Class Name'))
    application_property = forms.CharField(max_length=100,
                                           label=_('App Property'))
    application_policy = forms.CharField(max_length=100,
                                         label=_('App Policy'))

    class Meta:
        name = _('Details')


class SetClassDetails(workflows.Step):
    action_class = SetClassDetailsAction
    contributes = ['name', 'application_property', 'application_policy']


class CreateClass(workflows.Workflow):
    slug = 'create_class'
    name = _("Create Class")
    finalize_button_name = _("Create")
    success_message = _('Created Class')
    failure_message = _('Unable to add Class.')
    success_url = "horizon:network:flavor_app:index"
    default_steps = (SetClassDetails,)

    def handle(self, request, context):
        client = api.get_client(request)
        try:
            client.flavor_app.classes.create(**context)
            return True
        except Exception:
            return False
