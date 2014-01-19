import logging

from django.contrib.auth.models import AnonymousUser


LOG = logging.getLogger(__name__)


def set_session_from_user(request, user):
    request.session['jsessionid'] = user.jsessionid
    request.session['username'] = user.username
    request.session['user_id'] = user.id


def create_user_from_jsessionid(username, jsessionid, controller):
    return User(username=username,
                jsessionid=jsessionid,
                enabled=True,
                controller=controller)


class User(AnonymousUser):
    def __init__(self, username=None, enabled=False, jsessionid=None,
                 controller=None):
        self.id = username
        self.pk = username
        self.jsessionid = jsessionid
        self.username = username
        self.enabled = enabled
        self.controller = controller

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.username)

    def is_authenticated(self):
        return self.jsessionid is not None

    def is_anonymous(self):
        return not self.is_authenticated()

    @property
    def is_active(self):
        return self.enabled

    def save(*args, **kw):
        pass

    def delete(*args, **kw):
        pass
