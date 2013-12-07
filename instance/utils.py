# -*- coding: utf8 -*-
import logging

from lib.exception import ErrorException

from instance.models import Instance

from compute.models import Compute

logger = logging.getLogger("app")

def add(uid, cname, name, desc, flavour_name):
	exists = True
	try:
		ins = Instance.objects.get(name=name, uid=uid)
	except:
		exists = False

	if exists == False:
		try:
			flv = fl.get(flavour_name)
		except:
			raise ErrorException(404, "No flavour found")

		try:
			cte = Compute.objects.get(name=cname)
		except:
			raise ErrorException(404, "No compute found")

		ins = Instance()

		ins.uid = uid
		ins.name = name
		ins.desc = desc
		ins.vcpu = flv['vcpu']
		ins.disk = flv['disk']
		ins.memory = flv['memory']

		ins.compute = cte

		ins.save()
	else:
		raise ErrorException(500, "Unable to create new instance")

def edit(cname, iname, desc):
	try:
		cte = Compute.objects.get(name=cname)
	except Compute.DoesNotExist, e:
		raise ErrorException(404, "No compute found")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "No compute found")

	try:
		d = Instance.objects.get(compute=cte, name=iname)
	except Instance.DoesNotExist, e:
		raise ErrorException(404, "No instance found")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "No instance found")

	try:
		d.desc = desc

		d.save()
	except:
		raise ErrorException(500, "Unable to set instance")

def get(cname, iname):
	try:
		cte = Compute.objects.get(name=cname)
	except Compute.DoesNotExist, e:
		raise ErrorException(404, "No compute found")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "No compute found")

	try:
		d = Instance.objects.get(compute=cte, name=iname)
	except Instance.DoesNotExist, e:
		raise ErrorException(404, "No instance found")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "No instance found")

	return {
		'id': d.id,
		'uid': d.uid,
		'name': d.name,
		'desc': d.desc,
		'vcpu': d.vcpu,
		'disk': d.disk,
		'memory': d.memory,
		'task': d.task,
		'state': d.state,
		'power_state': d.power_state,
		'ipv4': d.ipv4,
		'ipv6': d.ipv6
	}

def get_all_by_compute(cname, uid=None):
	try:
		cte = Compute.objects.get(name=cname)
	except Compute.DoesNotExist, e:
		raise ErrorException(404, "No compute found")
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "No compute found")

	if uid is not None:
		_data = Instance.objects.filter(compute=cte, uid=uid)
	else:
		_data = Instance.objects.filter(compute=cte)

	data = []
	for d in _data:
		data.append({
			'id': d.id,
			'name': d.name,
			'desc': d.desc,
			'vcpu': d.vcpu,
			'disk': d.disk,
			'memory': d.memory,
			'task': d.task,
			'state': d.state,
			'power_state': d.power_state,
			'ipv4': d.ipv4,
			'ipv6': d.ipv6
		})

	return data

def get_all_ip(vers = 4):
	try:
		_data = Instance.objects.all()
	except Instance.DoesNotExist, e:
		_data = []
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "No instances found")

	data = []
	for d in _data:
		if vers == 4:
			data.append(d.ipv4)
		elif vers == 6:
			data.append(d.ipv6)

	return data
