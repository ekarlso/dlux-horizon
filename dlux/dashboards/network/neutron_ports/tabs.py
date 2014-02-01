# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 NEC Corporation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import tabs

from dlux.api import get_client

def get_ovs_ids(client, port_id):

    ovs_interface = _get_interface_id(client, port_id)
    ovs_port = _get_port_id(client, ovs_interface)
    ovs_bridge = _get_bridge_id(client, ovs_port)

    return { "interface_id" : ovs_interface,
             "port_id" : ovs_port,
             "bridge_id": ovs_bridge }


def _get_interface_id(client, port_id):
    connections = client.connection_manager.list()
    for n in connections:
        if n.type == 'OVS':
            data = client.ovsdb.list(n.type, n.id, 'interface')
            rows = data["rows"]
            for row in rows:
                uuid = row
                for items in rows[uuid]["external_ids"]:
                    if type(items) == list:
                        for item in items:
                            if item[0] == "iface-id":
                                if item[1] == port_id:
                                    return uuid

def _get_port_id(client, interface_id):
    connections = client.connection_manager.list()
    for n in connections:
        if n.type == 'OVS':
            data = client.ovsdb.list(n.type, n.id, 'port')
            rows = data["rows"]
            for row in rows:
                uuid = row
                for items in rows[uuid]["interfaces"]:
                    if type(items) == list:
                        for item in items:
                            if item[1] == interface_id:
                                return uuid

def _get_bridge_id(client, port_id):
    connections = client.connection_manager.list()
    for n in connections:
        if n.type == 'OVS':
            data = client.ovsdb.list(n.type, n.id, 'bridge')
            rows = data["rows"]
            for row in rows:
                uuid = row
                for items in rows[uuid]["ports"]:
                    if type(items) == list:
                        for item in items:
                            if item[1] == port_id:
                                return uuid


class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = "network/neutron_ports/_detail_overview.html"

    def get_context_data(self, request):
        port_id = self.tab_group.kwargs['port_id']
        client = get_client(self.request)
        port = client.neutron.ports.get(port_id)

        data = get_ovs_ids(client, port_id)
        data["port"] = port
        return data


class PortDetailTabs(tabs.TabGroup):
    slug = "port_details"
    tabs = (OverviewTab,)
