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


class SetPolicyDetailsAction(workflows.Action):
    name = forms.CharField(max_length=50, label=_('Policy Name'))
    tenant_uuid = forms.CharField(max_length=140, label=('Tenant ID'))
    flavor = forms.CharField(max_length=60, label=_('Flavor'))

    class Meta:
        name = _('Details')


class SetPolicyDetails(workflows.Step):
    action_class = SetPolicyDetailsAction
    contributes = ['name', 'tenant_uuid', 'flavor']


class CreatePolicy(workflows.Workflow):
    slug = 'create_policy'
    name = _("Create Policy")
    finalize_button_name = _("Create")
    success_message = _('Created Policy')
    failure_message = _('Unable to add policy.')
    success_url = "horizon:network:flavor_app:index"
    default_steps = (SetPolicyDetails,)

    def handle(self, request, context):
        client = api.get_client(request)
        try:
            client.flavor_app.policy.create(**context)
            return True
        except Exception:
            return False
