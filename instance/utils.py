# -*- coding: utf8 -*-
import logging

from lib.exception import ErrorException

from instance.models import Instance
from compute.models import Compute

import compute.utils as cteutils
import flavour.utils as flutils

logger = logging.getLogger("app")

def add(uid, cname, name, desc, flavour_name):
	exists = True
	try:
		ins = Instance.objects.get(name=name, uid=uid)
	except Instance.DoesNotExist, e:
		exists = False
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Error while testing instance duplication")

	if exists == False:
		try:
			flv = flutils.get(flavour_name)
		except Exception, e:
			logger.error(str(e))
			raise ErrorException(404, "No flavour found")

		try:
			cte = cteutils.get_obj(cname)
		except ErrorException, e:
			raise ErrorException(e.code, e.value)
		except Exception, e:
			logger.error(str(e))
			raise ErrorException(500, "")

		try:
			cte_ips = cteutils.get_all_ip_range(cname)
		except ErrorException, e:
			raise ErrorException(e.code, e.value)
		except Exception, e:
			logger.error(str(e))
			raise ErrorException(500, "")

		ins = Instance()

		ins.uid = uid
		ins.name = name
		ins.desc = desc
		ins.vcpu = flv['vcpu']
		ins.disk = flv['disk']
		ins.memory = flv['memory']

		ins.compute = cte

		try:
			ips_used = get_all_ips()
		except:
			ips_used = []

		if len(cte_ips) > 0:
			cte_ips = cte_ips[0]
			ipv4 = cteutils.get_next_ipv4(
				cte_ips['range_min'],
				cte_ips['range_max'],
				cte_ips['range_mask'],
				ips_used)

			if ipv4 is not None:
				ins.ipv4 = ipv4
			
				try:
					cte_ipsv6 = cteutils.get_all_ip_range(cname, 6)

					if len(cte_ipsv6) > 0:
						cte_ipsv6 = cte_ipsv6[0]

					ipv6 = cteutils.generate_ipv6_by_ipv4(cte_ipsv6['range_min'], ipv4)
					if ipv6 is not None:
						ins.ipv6 = ipv6
				except Exception, e:
					logger.error(str(e))
					pass

		ins.save()
	else:
		raise ErrorException(500, "Instance name already exists")

def edit(cname, iname, desc):
	try:
		cte = get_obj(cname)
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(e.code, e.value)

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

def get_all_ips(vers = 4):
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
