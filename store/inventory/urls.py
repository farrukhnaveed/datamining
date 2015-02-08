from django.conf.urls import patterns, include, url
from store.inventory.views import homepage


urlpatterns = patterns('',
  url( r'^$', homepage, { 'template_name': 'inventory/homepage.html' }, name = 'homepage' ),
  #(?P<name_slug>[-\w]+)
)
