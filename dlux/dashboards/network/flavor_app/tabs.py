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

class TestFlavor(object):
    def __init__(self, id, name, description, fwd_class):
        self.id = id
        self.name = name
        self.description = description
        self.fwd_class = fwd_class


class TestClass(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name


class TestPolicy(object):
    def __init__(self, id, tenant_uuid, flavor):
        self.id = id
        self.tenant_uuid = tenant_uuid
        self.flavor = flavor


class FlavorTab(tabs.TableTab):
    table_classes = [FlavorTable]
    name = _("Flavors")
    slug = "flavors"
    template_name = "horizon/common/_detail_table.html"

    def get_flavors_data(self):
        data = [ TestFlavor(1, "best effort", "Best Effort Traffic Class", 1),
                 TestFlavor(2, "bronze", "Bronze Traffic Class", 2),
                 TestFlavor(3, "silver", "Silver Traffic Class", 3),
                 TestFlavor(4, "gold", "Gold Traffic Class", 4),
                 TestFlavor(5, "platinum", "Platinum Traffic Class", 5),
               ]
        return data

class ClassTab(tabs.TableTab):
    table_classes = [ClassTable]
    name = _("Class")
    slug = "classes"
    template_name = "horizon/common/_detail_table.html"

    def get_class_data(self):
        data = [ TestClass(1, "Least Cost Path"),
                 TestClass(2, "Shortest Path"),
                 TestClass(3, "100Mbps Guaranteed"),
                 TestClass(4, "1Gbps Guaranteed"),
                 TestClass(5, "Lowest Latency Path"),
               ]
        return data


class PolicyTab(tabs.TableTab):
    table_classes = [PolicyTable]
    name = _("Policy")
    slug = "policy"
    template_name = "horizon/common/_detail_table.html"

    def get_policy_data(self):
        data = [ TestPolicy(1, "abcdefg123456", 1)]
        return data


class FlavorAppTabs(tabs.TabGroup):
    slug = "flavorapptab"
    tabs = (FlavorTab, ClassTab, PolicyTab)
    sticky = True
