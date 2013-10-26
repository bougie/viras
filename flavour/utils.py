#-*- coding: utf8 -*-

from flavour.models import Flavour

def add(name, vcpu, memory, disk):
	exists = True
	try:
		flv = Flavour.objects.get(name=name)
	except:
		exists = False

	if exists == False:
		flv = Flavour()

		flv.name = name
		flv.vcpu = vcpu
		flv.memory = memory
		flv.disk = disk

		flv.save()
	else:
		raise

def delete(name):
	try:
		flv = Flavour.objects.get(name=name)
		flv.delete()
	except:
		raise

def edit(name, vcpu, memory, disk):
	try:
		flv = Flavour.objects.get(name=name)

		flv.vcpu = vcpu
		flv.memory = memory
		flv.disk = disk

		flv.save()
	except:
		raise

def get(name):
	try:
		d = Flavour.objects.get(name=name)

		return {
			'id': d.id,
			'name': d.name,
			'vcpu': d.vcpu,
			'memory': d.memory,
			'disk': d.disk
		}
	except:
		raise

	return flv

def get_all():
	data = []

	try:
		_data = Flavour.objects.all()

		for d in _data:
			data.append({
				'id': d.id,
				'name': d.name,
				'vcpu': d.vcpu,
				'memory': d.memory,
				'disk': d.disk
			})
	except:
		raise

	return data
