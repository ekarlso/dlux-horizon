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


class OverviewTab(tabs.Tab):
    name = _("Overview")
    slug = "overview"
    template_name = "network/neutron_subnets/_detail_overview.html"

    def get_context_data(self, request):
        subnet_id = self.tab_group.kwargs['subnet_id']
        client = get_client(self.request)
        subnet = client.neutron.subnets.get(subnet_id)
        return { "subnet" : subnet }

class SubnetDetailTabs(tabs.TabGroup):
    slug = "subnet_details"
    tabs = (OverviewTab,)
