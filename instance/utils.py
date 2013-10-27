# -*- coding: utf8 -*-

from instance.models import Instance

from compute.models import Compute
import compute.utils as ct
import flavour.utils as fl

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
			raise

		try:
			cte = Compute.objects.get(name=cname)
		except:
			raise

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
		raise
