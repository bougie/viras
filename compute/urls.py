from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'compute.views.index'),
	url(r'^([0-9]+)$', 'compute.views.change'),
)
