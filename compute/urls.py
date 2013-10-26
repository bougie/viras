from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'compute.views.index'),
	url(r'^add/$', 'compute.views.add'),
)
