from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'flavour.views.index'),
	url(r'^(.+)/$', 'flavour.views.settings'),
	url(r'^(.+)$', 'flavour.views.settings'),
)
