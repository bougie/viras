from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^api$', 'keystore.views.api_index', name = 'api_index'),
	url(r'^api/(.+)/$', 'keystore.views.api_settings'),
	url(r'^api/(.+)$', 'keystore.views.api_settings', name = 'api_settings'),
	url(r'^consumer$', 'keystore.views.consumer_index'),
	url(r'^consumer/(.+)/$', 'keystore.views.consumer_settings'),
	url(r'^consumer/(.+)$', 'keystore.views.consumer_settings', name = 'consumer_settings'),
)
