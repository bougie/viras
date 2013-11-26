#-*- coding: utf8 -*-
import logging
import hashlib

from lib.response import ErrorResponse, OkResponse
from keystore.utils import api_get, consumer_get

logger = logging.getLogger("app")

def required_auth_query(a_view):
	def _wrapped_view(request, *args, **kwargs):
		body = request.body
		is_auth = False

		try:
			if 'HTTP_X_VIRAS_APPLICATION' in request.META:
				api = api_get(None, request.META['HTTP_X_VIRAS_APPLICATION'])

				if 'HTTP_X_VIRAS_CONSUMER' in request.META:
					cons = consumer_get(request.META['HTTP_X_VIRAS_CONSUMER'])

					s1 = hashlib.sha1()
					s1.update("+".join([
						api["api_secret"],
						cons["consumer_key"],
						body
					]))
					sig = "$1$" + s1.hexdigest()

					if 'HTTP_X_VIRAS_SIGNATURE' in request.META and request.META['HTTP_X_VIRAS_SIGNATURE'] == sig:
						is_auth = True
						
		except Exception, e:
			logger.error(str(e))

		if is_auth == True:
			return a_view(request, *args, **kwargs)
		else:
			return ErrorResponse(401)

	return _wrapped_view

