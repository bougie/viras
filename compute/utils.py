#-*- coding: utf8 -*-
from netaddr import *

import logging

from lib.exception import ErrorException
from compute.models import Compute, ComputeIpRange

logger = logging.getLogger("app")

def add(name, vcpu, memory, disk, ctype, ipv4 = None, ipv6 = None):
	exists = True
	try:
		cte = Compute.objects.get(name=name)
	except Compute.DoesNotExist, e:
		exists = False
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta create new compute")

	if exists == False:
		cte = Compute()

		cte.name = name
		cte.vcpu = vcpu
		cte.memory = memory
		cte.disk = disk
		cte.ctype = ctype
		cte.ipv4 = ipv4
		cte.ipv6 = ipv6

		try:
			cte.save()
		except:
			raise ErrorException(500, "Unable ta create new compute")
	else:
		raise ErrorException(404, "Unable ta get compute")

def add_ip_range(compute, rmin, rmax, rmask, mask, gw, vers):
	rip = ComputeIpRange()

	rip.range_min = rmin
	rip.range_max = rmax
	rip.range_mask = rmask
	rip.mask = mask
	rip.gw = gw
	rip.vers = vers

	rip.compute = compute

	try:
		rip.save()
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta set new ip range for the compute")

def delete(name):
	try:
		cte = get_obj(name)
	except ErrorException, e:
		raise ErrorException(e.code, e.value)

	try:
		cte.delete()
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable to get compute")

def edit(name, vcpu, memory, disk, ctype, ipv4, ipv6):
	try:
		cte = get_obj(name)
	except ErrorException, e:
		raise ErrorException(e.code, e.value)

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
		d = get_obj(name)
	except ErrorException, e:
		raise ErrorException(e.code, e.value)

	return {
		'id': d.id,
		'name': d.name,
		'vcpu': d.vcpu,
		'memory': d.memory,
		'disk': d.disk,
		'ctype': d.ctype
	}

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

def get_all_ip_range(cname, vers=None):
	data = []

	try:
		compute = get_obj(cname)
	except ErrorException, e:
		raise ErrorException(e.code, e.value)

	try:
		if vers is not None:
			_data = ComputeIpRange.objects.filter(compute=compute, vers=vers)
		else:
			_data = ComputeIpRange.objects.filter(compute=compute)

		for d in _data:
			data.append({
				'id': d.id,
				'range_min': d.range_min,
				'range_max': d.range_max,
				'range_mask': d.range_mask,
				'mask': d.range_mask,
				'gw': d.gw,
				'vers': d.vers
			})
	except Exception, e:
		logger.error(str(e))
		raise ErrorException(500, "Unable ta get compute's ips")

	return data

def get_next_ipv4(rmin, rmax, mask, ip_used = []):
	min_ip = IPAddress(rmin)
	min_ip_net = IPNetwork(rmin + '/' + mask)
	max_ip = IPAddress(rmax)
	max_ip_net = IPNetwork(rmax + '/' + mask)

	if min_ip_net.network == max_ip_net.network:
		ips_allowed = []

		for ip in list(min_ip_net):
			if ip >= min_ip and ip <= max_ip:
				if str(ip) not in ip_used:
					ips_allowed.append(ip)

		if len(ips_allowed) > 0:
			return str(ips_allowed[0])
		else:
			return None
	else:
		return None

def generate_ipv6_by_ipv4(ipv6_prefix, ipv4):
	try:
		ip = IPAddress(ipv4)
	except Exception, e:
		logger.error(str(e))
		return None

	ipv6 = ipv6_prefix + ':' + ipv4.replace('.', ':')
	try:
		return str(IPAddress(ipv6))
	except Exception, e:
		logger.error(str(e))
		return None
