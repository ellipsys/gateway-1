from django.conf.urls import patterns, url

from api import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^sensors$', views.sensors, name='index'),
    url(r'^sensors/(\d{4})$', views.sensors.detail, name='index')
)