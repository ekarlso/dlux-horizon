import logging

from django.contrib.auth.models import AnonymousUser


LOG = logging.getLogger(__name__)


def set_session_from_user(request, user):
    request.session['user_id'] = user.id


class User(AnonymousUser):
    def __init__(self, username=None, enabled=False, token=None,
                 endpoint=None):
        self.id = username
        self.pk = id
        self.username = username
        self.enabled = enabled
        token = 1
        self.token = token
        self.endpoint = endpoint

    def __unicode__(self):
        return self.username

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.username)

    def is_authenticated(self):
        return self.token is not None

    @property
    def is_active(self):
        return self.enabled

    def save(*args, **kw):
        pass

    def delete(*args, **kw):
        pass
