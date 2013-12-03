#-*- coding: utf8 -*-
import logging

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from lib.exception import ErrorException
from lib.token import generate

from keystore.models import ApiKey, ConsumerKey

logger = logging.getLogger("app")

def api_add(name, description):
	akey = ApiKey()

	akey.name = name
	akey.description = description

	akey.api_key = generate(16)
	akey.api_secret = generate(32)

	try:
		akey.save()

		return akey.api_key
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to create new api key")

def api_delete(aid):
	try:
		akey = ApiKey.objects.get(pk=aid)
	except ApiKey.DoesNotExist, e:
		raise ErrorException(404, "Unable to get api key")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get api key")

	try:
		akey.delete()
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to delete api key")

def api_exists(akey, asecret):
	ret = False

	try:
		nb_api = ApiKey.objects.filter(api_key=akey, api_secret=asecret).count()

		if nb_api == 1:
			ret = True
	except Exception, e:
		logger.error(str(e))
		pass

	return ret

def api_get(akey):
	try:
		key = ApiKey.objects.get(api_key=akey)

		return {
			'id': key.pk,
			'name': key.name,
			'description': key.description,
			'api_key': key.api_key,
			'api_secret': key.api_secret
		}
	except ApiKey.DoesNotExist, e:
		raise ErrorException(404, "Unable to get api key")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get api key")

def api_get_all():
	try:
		keys = ApiKey.objects.all()

		keys_list = []
		for k in keys:
			keys_list.append({
				'id': k.pk,
				'name': k.name,
				'description': k.description,
				'api_key': key.api_key,
				'api_secret': key.api_secret
			})

		return keys_list
	except ApiKey.DoesNotExist, e:
		raise ErrorException(404, "Unable to get api keys")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get api keys")

def consumer_add(login, password):
	ckey = ConsumerKey()

	try:
		user = authenticate(username=login, password=password)
	except Exception, e:
		print str(e)
		raise ErrorException(403, "Unable to authenticate the user")

	if user is not None:
		ckey.user = user
		ckey.consumer_key = generate(32)
		ckey.expiration = 0

		try:
			ckey.save()

			return ckey.consumer_key
		except Exception, e:
			logger.error(str(e))
			raise ErrorException(500, "Unable to create new consumer key")
	else:
		raise ErrorException(403, "Unable to authenticate the user")

def consumer_delete(cid):
	try:
		ckey = ConsumerKey.objects.get(pk=cid)
	except ConsumerKey.DoesNotExist, e:
		raise ErrorException(404, "Unable to get consumer key")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get consumer key")

	try:
		ckey.delete()
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to delete consumer key")

def consumer_get(cid, get_user=None):
	try:
		key = ConsumerKey.objects.get(consumer_key=cid)

		if get_user is not None and get_user == True:
			return {
				'id': key.pk,
				'expiration': key.expiration,
				'consumer_key': key.consumer_key,
				'user': key.user
			}
		else:
			return {
				'id': key.pk,
				'expiration': key.expiration,
				'consumer_key': key.consumer_key
			}
	except ConsumerKey.DoesNotExist, e:
		raise ErrorException(404, "Unable to get consumer key")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get consumer key")

def consumer_get_all():
	try:
		keys = ConsumerKey.objects.all()

		keys_list = []
		for k in keys:
			keys_list.append({
				'id': k.pk,
				'expiration': k.expiration,
				'consumer_key': k.consumer_key
			})

		return keys_list
	except COnsumerKey.DoesNotExist, e:
		raise ErrorException(404, "Unable to get consumer keys")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get consumer keys")
