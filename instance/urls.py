from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^(.+)/instance$', 'compute.views.index'),
	url(r'^(.+)/instance/$', 'compute.views.index'),
)
