#-*- coding: utf8 -*-

from flavour.models import Flavour

def add(name, vcpu, memory, disk):
	exists = True
	try:
		flv = Flavour.objects.get(name=name)
	except Flavour.DoesNotExist, e:
		exists = False
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta create new flavour")

	if exists == False:
		flv = Flavour()

		flv.name = name
		flv.vcpu = vcpu
		flv.memory = memory
		flv.disk = disk

		try:
			flv.save()
		except Exception, e:
			logger.error(str(e))
			raise ErrorException(500, "Unable to create new flavour")
	else:
		raise ErrorException(404, "Unable to create new flavour")

def delete(name):
	try:
		flv = Flavour.objects.get(name=name)
	except Flavour.DoesNotExist, e:
		raise ErrorException(404, "Unable to get flavour")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get flavour")

	try:
		flv.delete()
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to delete flavour")

def edit(name, vcpu, memory, disk):
	try:
		flv = Flavour.objects.get(name=name)
	except Flavour.DoesNotExist, e:
		raise ErrorException(404, "Unable to get flavour")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get flavour")

	try:
		flv.vcpu = vcpu
		flv.memory = memory
		flv.disk = disk

		flv.save()
	except:
		raise ErrorException(500, "Unable to set flavour")

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
	except Flavour.DoesNotExist, e:
		raise ErrorException(404, "Unable to get flavour")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get flavour")

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
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get flavours")

	return data
