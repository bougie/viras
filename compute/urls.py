from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'compute.views.index'),
	url(r'^(.+)/instance/$', 'instance.views.index'),
	url(r'^(.+)/instance$', 'instance.views.index'),
	url(r'^(.+)/$', 'compute.views.settings'),
	url(r'^(.+)$', 'compute.views.settings'),
)
