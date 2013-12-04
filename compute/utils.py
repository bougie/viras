#-*- coding: utf8 -*-
import logging

from lib.exception import ErrorException

from compute.models import Compute

logger = logging.getLogger("app")

def add(name, vcpu, memory, disk, ctype, ipv4 = None, ipv6 = None):
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
		cte.ipv4 = ipv4
		cte.ipv6 = ipv6

		cte.save()
	else:
		raise ErrorException(500, "Unable ta create new compute")

def delete(name):
	try:
		cte = Compute.objects.get(name=name)
		cte.delete()
	except Exception, e:
		logger.error(str(e))
		raise

def edit(name, vcpu, memory, disk, ctype, ipv4, ipv6):
	try:
		cte = Compute.objects.get(name=name)
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(404, "Unable ta get compute")

	try:
		cte.vcpu = vcpu
		cte.memory = memory
		cte.disk = disk
		cte.ctype = ctype
		cte.ipv4 = ipv4
		cte.ipv6 = ipv6

		cte.save()
	except Exception, e:
		logger.error(str(e))
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
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta get compute")

	return cte

def get_obj(name):
	try:
		return Compute.objects.get(name=name)
	except Compute.DoesNotExist, e:
		raise ErrorException(404, "Unable to get compute")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta get compute")

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
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta get computes")

	return data

def add_range_ips(compute, rmin, rmax, rmask, mask):
	rip = ComputeIpRange()

	rip.range_min = rmin
	rip.range_max = rmax
	rip.range_mask = rmask
	rip.mask = mask

	try:
		rip.save()
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta set new ip range for the compute")
