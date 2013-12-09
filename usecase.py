#-*- coding: utf8 -*-
from lib.request import Api

if __name__ == "__main__":
	api = Api("http://127.0.0.1:8000", "194939bB791b4652", "e7a0e2546A864bf5b5f03AD965F0b882", "7e465fceecb64893BCd2Bcb3C2efAC11")

	print "Ajout d'un compute :"
	data = {
		'name': 'prime',
		'vcpu': '8',
		'memory': '64000',
		'disk': '144',
		'ctype': 'xen'
	}
	api.post('/compute/', data)
	print api.get('/compute/')
	print

	print "Creation d'un range IPv4 et IPv6 :"
	data = {
		'range_min': '172.16.42.1',
		'range_max': '172.16.42.253',
		'range_mask': '255.255.255.0',
		'mask': '255.255.255.0',
		'gw': '172.16.42.254',
		'vers': 4
	}
	api.post('/compute/prime/iprange', data)
	
	data = {
		'range_min': '4242:470:cb19:e',
		'range_max': '4242:470:cb19:e',
		'range_mask': '64',
		'mask': '64',
		'gw': '4242:470:cb19:e:172.16.42.254',
		'vers': 6
	}
	api.post('/compute/prime/iprange', data)
	print api.get('/compute/prime/iprange')
	print

	print "Ajout d'un flavour :"
	data = {
		'name': 'small',
		'vcpu': '1',
		'memory': '512',
		'disk': '4'
	}
	api.post('/flavour/', data)
	print api.get('/flavour/')
	print

	print "Ajout de plusieurs instances :"
	for x in range(1, 6):
		data = {
			'name': 'fubar10' + str(x),
			'desc': 'Instance de teste 10' + str(x),
			'flavour': 'small'
		}
		print "    - instance fubar10" + str(x)
		api.post('/compute/prime/instance/', data)

	print api.get('/compute/prime/instance/')
