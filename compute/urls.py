from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'account.views.index', name='account_index'),
	url(r'^login/$', 'account.views.login', name='account_login'),
	url(r'^logout/$', 'account.views.logout', name='account_logout'),
	url(r'^passowrd/$', 'account.views.password', name='account_password'),
	url(r'^passowrd/([a-zA-Z0-9]{42})$', 'account.views.passwordValid', name='account_passwordValid'),
)
