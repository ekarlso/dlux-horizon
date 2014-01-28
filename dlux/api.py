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
import requests

from django.conf import settings
from odlclient.v2 import client as odl_client


def get_client(request):
    session = requests.Session()
    session.cookies.update({
        'JSESSIONID': request.user.jsessionid,
        'JSESSIONIDSSO': request.user.jsessionidsso
    })
    url = request.user.controller + '/controller/nb/v2'
    http = odl_client.HTTPClient(url, http=session, debug=settings.DEBUG)
    client = odl_client.Client(http)
    return client