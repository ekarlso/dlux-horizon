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
from horizon import tabs as horizon_tabs

from dlux.api import get_client
from dlux.dashboards.network.neutron_networks import tables


class IndexView(horizon_tables.DataTableView):
    template_name = "network/neutron_networks/index.html"
    table_class = tables.NeutronNetworksTable

    def get_data(self):
        client = get_client(self.request)
        return client.neutron.networks.list()

class DetailView(horizon_tables.DataTableView):
    template_name = 'network/neutron_networks/detail.html'
    table_class = tables.NeutronNetworkDetailTable
