import logging
import requests

from django.conf import settings

from dlux import exceptions
from dlux.auth.user import create_user_from_jsessionid

LOG = logging.getLogger(__name__)


class ControllerBackend(object):

    def get_user(self, user_id):
        if (hasattr(self, 'request') and
                user_id == self.request.session['user_id']):
            jsessionid = self.request.session['jsessionid']
            jsessionidsso = self.request.session['jsessionidsso']
            controller = self.request.session['controller_endpoint']
            user = create_user_from_jsessionid(user_id, jsessionid, jsessionidsso, controller)
            return user
        else:
            return None

    def authenticate(self, request=None, username=None, password=None,
                     controller_url=None):

        insecure = getattr(settings, 'SSL_NO_VERIFY', False)

        url = controller_url + settings.AUTH_PATH
        response = requests.get(url, auth=(username, password))

        if response.status_code == 401:
            LOG.warning('Authentication failure...')
            raise exceptions.AuthException('Invalid username or password. Please check your credentials and try again.')

        try:
            user = create_user_from_jsessionid(username=username,
                                               controller=controller_url,
                                               jsessionid=response.cookies.get('JSESSIONID'),
                                               jsessionidsso=response.cookies.get('JSESSIONIDSSO'),
                                               )
        except Exception as e:
            print e
            raise

        if request is not None:
            request.user = user

        return user
