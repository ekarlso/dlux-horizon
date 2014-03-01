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
from django.conf.urls import include  # noqa
from django.conf.urls import patterns  # noqa
from django.conf.urls import url  # noqa

from dlux.dashboards.network.flavor_app import views
from dlux.dashboards.network.flavor_app.flavors import urls as flavors_urls
from dlux.dashboards.network.flavor_app.classes import urls as classes_urls
from dlux.dashboards.network.flavor_app.policy import urls as policy_urls

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'flavors', include(flavors_urls, namespace='flavors')),
    url(r'classes', include(classes_urls, namespace='classes')),
    url(r'policy', include(policy_urls, namespace='policy'))

)
