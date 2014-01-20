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
from django.utils.translation import ugettext_lazy as _

from horizon import tables

from dlux.api import get_client
from dlux.utils import filters


class DeleteConnection(tables.BatchAction):
    name = "delete"
    action_present = _("Delete")
    action_past = _("Deletig connection")
    data_type_singular = _("Connection")
    data_type_plural = _("Connections")
    classes = ('btn-danger', 'btn-terminate')

    def action(self, request, obj_id):
        client = get_client(request)
        node_id, node_type = obj_id.split('%')
        client.connection_manager.delete(node_type, node_id)


class LaunchLink(tables.LinkAction):
    name = "launch"
    verbose_name = _("Create Connection")
    url = "horizon:network:connections:create"
    classes = ("btn-launch", "ajax-modal")


class ConnectionsTable(tables.DataTable):
    id = tables.Column('id', verbose_name='Identifier')
    type = tables.Column('type', verbose_name='Type')

    class Meta:
        name = "connections"
        verbose_name = _('Connections')
        table_actions = (LaunchLink, DeleteConnection,)

    def get_object_id(self, datum):
        return filters.keys_as_id(datum, keys=['id', 'type'])
