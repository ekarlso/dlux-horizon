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

from horizon import tables
from dlux.api import get_client


class CreateClassLink(tables.LinkAction):
    name = "create_class"
    verbose_name = _("Create Class")
    url = "horizon:network:flavor_app:classes:create"
    classes = ("btn-launch", "ajax-modal")


class DeleteClass(tables.DeleteAction):
    data_type_singular = 'Class'
    data_type_plugar = 'Classes'

    def delete(self, request, obj_id):
        client = get_client(request)
        client.flavor_app.classes.delete(obj_id)


class ClassTable(tables.DataTable):
    id = tables.Column('id', verbose_name=_('Id'))
    name = tables.Column('name', verbose_name=_('Name'))

    class Meta:
        name = 'class'
        verbose_name = _('Class')
        table_actions = (CreateClassLink, DeleteClass,)

    def get_object_id(self, datum):
        return datum.id
