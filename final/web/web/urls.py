"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from django.contrib import admin
from concert.views import index,ticket,concert,subscribe,ticket2,detail,item
from api.views import getPTT,getPTTnum,getConcert,addSubscribe,getSubscribe,delSubscribe

admin.autodiscover()

urlpatterns = [
	url(r'^accounts/', include('allauth.urls')),
	url(r'^$',index),
	url(r'^ticket/',ticket),
	url(r'^ticket2/(?P<id>[0-9]+)/$',ticket2),
	url(r'^concert/',concert),
	url(r'^item/',item),
	url(r'^detail/(?P<id>[0-9]+)/$',detail),
	url(r'^subscribe/',subscribe),
	url(r'^api/getConcert/',getConcert),
	url(r'^api/getPTT/',getPTT),
    url(r'^api/getPTTnum/',getPTTnum),
	url(r'^api/addSubscribe/',addSubscribe),
	url(r'^api/getSubscribe/',getSubscribe),
	url(r'^api/delSubscribe/(?P<id>[0-9]+)/$', delSubscribe),
	url(r'^admin/', admin.site.urls),
    url(r'^mail-queue/', include('mailqueue.urls')),
]
