from django.conf.urls import patterns, include, url
from django.contrib import admin
from RPiPowerController.actions import  turnOff, turnOn

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RPiPowerController.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^turnOn/', turnOn),
    url(r'^turnOff/', turnOff),
)
