from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('securesync.api_views',
    url(r'^api/register$', 'register_public_key', {}, 'register_public_key'),
    url(r'^api/session/create$', 'create_session', {}, 'create_session'),
    url(r'^api/session/destroy$', 'destroy_session', {}, 'destroy_session'),
    url(r'^api/models/count$', 'count_models', {}, 'count_models'),
    url(r'^api/models/update$', 'update_models', {}, 'update_models'),
)

urlpatterns += patterns('securesync.views',
    url(r'^register/$', 'register_device', {}, 'register_device'),
    url(r'^adduser/$', 'add_facility_user', {}, 'add_facility_user'),
    url(r'^login/$', 'login', {}, 'login'),
    url(r'^logout/$', 'logout', {}, 'logout'),
)
