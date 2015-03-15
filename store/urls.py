from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('store.registration.urls')),
	url(r'^', include('store.inventory.urls')),
	url(r'^', include('store.transactions.urls')),
	#url(r'^transaction/', include('store.transactions.urls')),
)

urlpatterns += patterns("",
	url(r'^site_media/media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT,
	}),
	
	url(r'^site_media/static/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.PROJECT_ROOT + '/project_static/',
	}),
)