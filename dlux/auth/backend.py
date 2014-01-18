import logging
import requests

from django.conf import settings

from dlux import exceptions
from dlux.auth.user import User


LOG = logging.getLogger(__name__)


class ControllerBackend(object):
    # NOTE: This method doesn't work atm
    def get_user(self, user_id):
        if user_id == self.request.session['user_id']:
            return self.request.session['user']
        else:
            return None

    def authenticate(self, request=None, username=None, password=None,
                     controller_url=None):
        print "authentiating... with", locals()
        insecure = getattr(settings, 'SSL_NO_VERIFY', False)

        url = controller_url + settings.AUTH_PATH
        print "url is %s" % url

        resp = requests.get(url, auth=(username, password))
        print "authed with ctl and got an %i" % resp.status_code

        if resp.status_code == 401:
            LOG.warning("Authentication failure %s" % resp.text)
            raise exceptions.AuthException

        try:
            user = User(
                username=username,
                endpoint=controller_url,
                token=resp.cookies.get('JSESSIONID'))
        except Exception as e:
            print e
            raise

        if request is not None:
            request.user = user

        return user
