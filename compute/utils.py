#-*- coding: utf8 -*-
from lib.exception import ErrorException

from compute.models import Compute

def add(name, vcpu, memory, disk, ctype):
	exists = True
	try:
		cte = Compute.objects.get(name=name)
	except:
		exists = False

	if exists == False:
		cte = Compute()

		cte.name = name
		cte.vcpu = vcpu
		cte.memory = memory
		cte.disk = disk
		cte.ctype = ctype

		cte.save()
	else:
		raise ErrorException(500, "Unable ta create new compute")

def delete(name):
	try:
		cte = Compute.objects.get(name=name)
		cte.delete()
	except:
		raise

def edit(name, vcpu, memory, disk, ctype):
	try:
		cte = Compute.objects.get(name=name)
	except:
		raise ErrorException(404, "Unable ta get compute")

	try:
		cte.vcpu = vcpu
		cte.memory = memory
		cte.disk = disk
		cte.ctype = ctype

		cte.save()
	except:
		raise ErrorException(500, "Unable ta set compute")

def get(name):
	try:
		d = Compute.objects.get(name=name)

		return {
			'id': d.id,
			'name': d.name,
			'vcpu': d.vcpu,
			'memory': d.memory,
			'disk': d.disk,
			'ctype': d.ctype
		}
	except:
		raise ErrorException(500, "Unable ta get compute")

	return cte

def get_all():
	data = []

	try:
		_data = Compute.objects.all()

		for d in _data:
			data.append({
				'id': d.id,
				'name': d.name,
				'vcpu': d.vcpu,
				'memory': d.memory,
				'disk': d.disk,
				'ctype': d.ctype
			})
	except:
		raise ErrorException(500, "Unable ta get computes")

	return data
