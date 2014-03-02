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

from horizon import tabs

from dlux.api import get_client
from dlux.dashboards.network.flavor_app.flavors.tables import FlavorTable
from dlux.dashboards.network.flavor_app.classes.tables import ClassTable
from dlux.dashboards.network.flavor_app.policy.tables import PolicyTable


class FlavorTab(tabs.TableTab):
    table_classes = [FlavorTable]
    name = _("Flavors")
    slug = "flavors"
    template_name = "horizon/common/_detail_table.html"

    def get_flavors_data(self):
        client = get_client(self.request)
        return client.flavor_app.flavors.list()

class ClassTab(tabs.TableTab):
    table_classes = [ClassTable]
    name = _("Class")
    slug = "classes"
    template_name = "horizon/common/_detail_table.html"

    def get_class_data(self):
        client = get_client(self.request)
        return client.flavor_app.classes.list()


class PolicyTab(tabs.TableTab):
    table_classes = [PolicyTable]
    name = _("Policy")
    slug = "policy"
    template_name = "horizon/common/_detail_table.html"

    def get_policy_data(self):
        client = get_client(self.request)
        return client.flavor_app.policy.list()


class FlavorAppTabs(tabs.TabGroup):
    slug = "flavorapptab"
    tabs = (FlavorTab, ClassTab, PolicyTab)
    sticky = True
