from django.conf.urls import patterns, include, url
from store.transactions.views import add_item, cart, checkout


urlpatterns = patterns('',
	url( r'^cart/ajax/add/$', add_item, name = 'add_item' ),
	url( r'^cart/$', cart, { 'template_name': 'transactions/cart.html' }, name = 'cart' ),
	url( r'^checkout/$', checkout, name = 'checkout' ),
	# url( r'^category/(?P<category_slug>[-\w]+)/(?P<sub_category_slug>[-\w]+)/$', sub_category, { 'template_name': 'inventory/category.html' }, name = 'sub_category' ),
)
