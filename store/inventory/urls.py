from django.conf.urls import patterns, include, url
from store.inventory.views import homepage, category, sub_category, item


urlpatterns = patterns('',
  url( r'^$', homepage, { 'template_name': 'inventory/homepage.html' }, name = 'homepage' ),
  url( r'^category/(?P<category_slug>[-\w]+)/$', category, { 'template_name': 'inventory/category.html' }, name = 'category' ),
  url( r'^category/(?P<category_slug>[-\w]+)/(?P<sub_category_slug>[-\w]+)/$', sub_category, { 'template_name': 'inventory/category.html' }, name = 'sub_category' ),
  url( r'^category/(?P<category_slug>[-\w]+)/(?P<sub_category_slug>[-\w]+)/(?P<item_slug>[-\w]+)/$', item, { 'template_name': 'inventory/item.html' }, name = 'item' ),
)
