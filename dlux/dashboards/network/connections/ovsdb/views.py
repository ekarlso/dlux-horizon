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
from django.http import HttpResponse
from django.views import generic

from dlux.api import get_client
from django.utils.translation import ugettext_lazy as _

import simplejson as json

from dlux.dashboards.network.connections.ovsdb.tables import TABLES

class RowsView(generic.View):
    def get(self, request, node_type, node_id, table, row=None):
        client = get_client(request)

        if row is not None:
            data = client.ovsdb.get(node_type, node_id, table, row)
        else:
            data = client.ovsdb.list(node_type, node_id, table)

        tmp = TABLES.get(table)
        tmp["table"]["rows"] = data["rows"]

        return HttpResponse(
            json.dumps(tmp), content_type='application/json')
