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

from django.core import urlresolvers
from django.utils.translation import ugettext_lazy as _
from horizon import tables

from dlux.utils.filters import keys_as_id

STATES = {0: 'DOWN', 1: 'UP'}

def get_network_link(datum):
    view = "horizon:network:neutron_networks:detail"
    if datum.id:
        #ToDo: Not sure why this works, but it does
        link = urlresolvers.reverse(view, args={datum.id})
    else:
        link = None
    return link

class NeutronNetworksTable(tables.DataTable):
    id = tables.Column('id',
                       verbose_name=_('Identifier'),
                       link=get_network_link)
    name = tables.Column('name', verbose_name=_('Name'))
    tenant_id = tables.Column('tenant_id', verbose_name=_("Tenant Identifier"))
    type = tables.Column('provider:network_type',
        verbose_name=_("Provider Network Type"))
    segmentation_id = tables.Column('provider:segmentation_id',
        verbose_name=_("Segmentation ID"))
    status = tables.Column('status', verbose_name=_("Status"))

    class Meta:
        name = 'neutron_networks'
        verbose_name = _('Neutron Networks')

    def get_object_id(self, datum):
        return datum.id

class NeutronNetworkDetailTable(tables.DataTable):
    id = tables.Column('id', verbose_name=_('Identifier'))
    name = tables.Column('name', verbose_name=_('Name'))
    tenant_id = tables.Column('tenant_id', verbose_name=_("Tenant Identifier"))

    class Meta:
        name = 'neutron_networks'
        verbose_name = _('Neutron Networks')




