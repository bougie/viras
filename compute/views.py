#-*- coding: utf8 -*-

from django.http import HttpResponse
from django.utils import simplejson

from compute.models import Compute

def index(request):
	if request.method == 'GET':
		response_data = {}

		data = Compute.objects.all()
		if len(data) == 0:
			data = ['']

		response_data = {
			"results": data
		}
		return HttpResponse(simplejson.dumps(response_data), content_type="application/json")
	else:
		return HttpResponse(status=501)
