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
from django import http
from django.views import generic
from jolokiaclient.client import Client
from jolokiaclient.client import make_requests
import simplejson as json

from dlux.api import get_client


class IndexView(generic.TemplateView):
    template_name = 'system/overview/index.html'

    def get_context_data(self):
        {}


class StatsView(generic.View):
    def get(self, request):
        client = get_client(request)
        jolokia = Client(
            client.http_client,
            jolokia_base='/controller/nb/v2/jolokia')

        elements = ['Memory', 'Threading']

        reqs = []
        for i in elements:
            reqs.append({'type': 'read', 'mbean': 'java.lang:type=%s' % i})

        response = jolokia.do_requests(make_requests(reqs))

        data = {}
        for i in xrange(0, len(elements)):
            data[elements[i].lower()] = response[i]['value']

        return http.HttpResponse(
            json.dumps(data), content_type='application/json')
