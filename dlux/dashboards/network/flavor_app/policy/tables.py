# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Author: Dave Tucker <dave.j.tucker@hp.com>
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
from django.utils.translation import ugettext_lazy as _

from horizon import tables
from dlux.api import get_client


class CreatePolicyLink(tables.LinkAction):
    name = "create_Policy"
    verbose_name = _("Create Policy")
    url = "horizon:network:flavor_app:policy:create"
    classes = ("btn-launch", "ajax-modal")


class DeletePolicy(tables.DeleteAction):
    data_type_singular = 'Policy'
    data_type_plugar = 'Policys'

    def delete(self, request, obj_id):
        client = get_client(request)
        client.flavor_app.policy.delete(obj_id)


class PolicyTable(tables.DataTable):
    id = tables.Column('id', verbose_name=_('Id'))
    tenant_uuid = tables.Column('tenant_uuid', verbose_name=_('Tenant ID'))
    flavor = tables.Column('flavor', verbose_name=_('Flavor'))

    class Meta:
        name = 'policy'
        verbose_name = _('Policy')
        table_actions = (CreatePolicyLink, DeletePolicy,)

    def get_object_id(self, datum):
        return datum.id
