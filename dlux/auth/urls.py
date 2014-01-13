from django.conf.urls.defaults import patterns, url

from dlux.auth.utils import patch_middleware_get_user

patch_middleware_get_user()

urlpatterns = patterns(
    'dlux.auth.views',
    url(r"^login/$", "login", name='login'),
    url(r"^logout/$", 'logout', name='logout'),
)
