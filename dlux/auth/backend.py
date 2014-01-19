import logging
import requests

from django.conf import settings

from dlux import exceptions
from dlux.auth.user import create_user_from_jsessionid

LOG = logging.getLogger(__name__)


class ControllerBackend(object):
    # NOTE: This method doesn't work atm
    def get_user(self, user_id):
        if (hasattr(self, 'request') and
                user_id == self.request.session["user_id"]):
            username = self.request.session['username']
            jsessionid = self.request.session['jsessionid']
            controller = self.request.session['controller_endpoint']
            user = create_user_from_jsessionid(username, jsessionid, controller)
            return user
        else:
            return None
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
            user = create_user_from_jsessionid(username=username,
                                               controller=controller_url,
                                               jsessionid=resp.cookies.get('JSESSIONID'))
        except Exception as e:
            print e
            raise

        if request is not None:
            request.user = user

        return user
