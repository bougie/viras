#-*- coding: utf8 -*-

from django.core.exceptions import ImproperlyConfigured

from keystore.utils import consumer_get

class TokenAuthentication(object):
	header = 'HTTP_X_VIRAS_CONSUMER'

	def process_request(self, request):
		if not hasattr(request, 'user'):
			raise ImproperlyConfigured(
				"The Django token user auth middleware requires the"
				" authentication middleware to be installed.  Edit your"
				" MIDDLEWARE_CLASSES setting to insert"
				" 'auth.middleware.TokenAuthentication'"
				" before the RemoteUserMiddleware class.")

		try:
			consumer_key = request.META[self.header]
		except KeyError:
			return

		try:
			consumer = consumer_get(cid = consumer_key, get_user = True)

			if consumer:
				request.user = consumer['user']
		except:
			return
