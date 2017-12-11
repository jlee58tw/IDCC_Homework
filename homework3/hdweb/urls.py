from django.conf.urls import include, url
from django.contrib.auth.models import User
from django.contrib import admin
from accounts.views import login, logout, index
from job.views import upload, display, job, execute, delete, status


urlpatterns = [
	url(r'^$',index),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$',login),
	url(r'^accounts/logout/$',logout),
	url(r'^index/$',index),
	url(r'^upload/$', upload, name='upload'),
	url(r'^job/$', job),
	url(r'^execute/$', execute),
	url(r'^status/$', status),
	url(r'^delete/(?P<id>[0-9]+)/$', delete),
]
