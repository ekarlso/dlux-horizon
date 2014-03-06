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

import sys

from horizon.test.settings import *  # noqa
from horizon.utils import secret_key

from dlux import exceptions

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.abspath(os.path.join(TEST_DIR, "../../"))

SECRET_KEY = secret_key.generate_or_read_from_file(
    os.path.join(TEST_DIR, '.secret_key_store'))
ROOT_URLCONF = 'dlux.urls'

if ROOT_PATH not in sys.path:
    sys.path.append(ROOT_PATH)

TEMPLATE_DIRS = (
    os.path.join(TEST_DIR, 'templates'),
)

INSTALLED_APPS = [
    'dlux',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'compressor',
    'horizon',
    'dlux.dashboards.network.dashboard',
    'dlux.auth',
]

AUTHENTICATION_BACKENDS = ('dlux.auth.backend.ControllerBackend',)

SITE_BRANDING = 'OpenDaylight - User eXperience - DLUX'
LOGIN_URL = '/auth/login/'
LOGOUT_URL = '/auth/logout/'
AUTH_PATH = '/controller/nb/v2/connectionmanager/nodes'
LOGIN_REDIRECT_URL = '/'
MEDIA_ROOT = os.path.abspath(os.path.join(ROOT_PATH, 'media'))
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.abspath(os.path.join(ROOT_PATH, 'static'))
STATIC_URL = '/static/'
COMPRESS_ROOT = STATIC_ROOT

HORIZON_CONFIG = {
    'dashboards': ('network',),
    'default_dashboard': 'network',
    'user_home': 'dlux.views.get_user_home',
    'ajax_queue_limit': 10,
    'auto_fade_alerts': {
        'delay': 3000,
        'fade_duration': 1500,
        'types': ['alert-success', 'alert-info']
    },
    'help_url': "http://docs.openstack.org",
    'exceptions': {'recoverable': exceptions.RECOVERABLE,
                   'not_found': exceptions.NOT_FOUND,
                   'unauthorized': exceptions.UNAUTHORIZED},
}

DEFAULT_CONTROLLER = ("http://localhost:8080", "localhost")
AVAILABLE_CONTROLLERS = [
    ("http://odl.cloudistic.me:8080/", "Cloudistic")
]

NOSE_ARGS = ['--nocapture',
             '--nologcapture',
             '--cover-package=dlux',
             '--cover-inclusive',
             '--all-modules']

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/less', ('lessc {infile}')),
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
)

COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'dashboard'
COMPRESS_CSS_HASHING_METHOD = 'hash'
COMPRESS_PARSER = 'compressor.parser.HtmlParser'


COMPRESS_PRECOMPILERS = (
    ('text/less', ('lessc {infile}')),
)

COMPRESS_CSS_FILTERS = (
    'compressor.filters.css_default.CssAbsoluteFilter',
)

COMPRESS_ENABLED = True
COMPRESS_OUTPUT_DIR = 'dashboard'
COMPRESS_CSS_HASHING_METHOD = 'hash'
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
