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
from django.shortcuts import render_to_response

from horizon import tabs

from dlux.api import get_client
from dlux.dashboards.network.nodes import tables


class OvsdbTab(tabs.Tab):
    name = _("OVSDB")
    slug = "ovsdb"
    template_name = "network/connections/ovsdb.html"

    def get_context_data(self, request):
        return {}


class DetailTabs(tabs.TabGroup):
    slug = "access_security_tabs"
    tabs = (OvsdbTab,)
    sticky = True
