from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	(r'compute/', include('compute.urls')),
	(r'flavour/', include('flavour.urls')),
	(r'key/', include('keystore.urls')),
	url(r'auth$', 'auth.views.authenticate'),
)

urlpatterns += staticfiles_urlpatterns()
