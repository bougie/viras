from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'account.views.index', name='compute_index'),
)
