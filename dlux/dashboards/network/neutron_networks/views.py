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

from horizon import tables as horizon_tables
from horizon.utils import memoized

from dlux.api import get_client
from dlux.dashboards.network.neutron_networks import tables
from dlux.dashboards.network.neutron_ports import tables as port_tables
from dlux.dashboards.network.neutron_subnets import tables as subnet_tables


class IndexView(horizon_tables.DataTableView):
    template_name = "network/neutron_networks/index.html"
    table_class = tables.NeutronNetworksTable

    def get_data(self):
        client = get_client(self.request)
        return client.neutron.networks.list()


class DetailView(horizon_tables.MultiTableView):
    table_classes = (subnet_tables.NeutronSubnetsTable,
                     port_tables.NeutronPortsTable)
    template_name = 'network/neutron_networks/detail.html'

    def get_neutron_subnets_data(self):
        network_id = self.kwargs['network_id']
        client = get_client(self.request)
        subnet_list = client.neutron.subnets.list()

        subnets = []
        for s in subnet_list:
            if s.network_id == network_id:
                subnets.append(s)

        return subnets

    def get_neutron_ports_data(self):
        network_id = self.kwargs['network_id']
        client = get_client(self.request)
        port_list = client.neutron.ports.list()

        ports = []
        for p in port_list:
            if p.network_id == network_id:
                ports.append(p)

        return ports

    @memoized.memoized_method
    def _get_data(self):
        network_id = self.kwargs['network_id']
        client = get_client(self.request)
        network = client.neutron.networks.get(network_id)
        return network

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["network"] = self._get_data()
        return context
