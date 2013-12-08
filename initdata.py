#-*- coding: utf8 -*-
from lib.request import Api

if __name__ == "__main__":
	api = Api("http://127.0.0.1:8000", "194939bB791b4652", "e7a0e2546A864bf5b5f03AD965F0b882", "7e465fceecb64893BCd2Bcb3C2efAC11")

	print "Ajout d'un compute"
	data = {
		'name': 'prime',
		'vcpu': '8',
		'memory': '64000',
		'disk': '144',
		'ctype': 'xen'
	}
	api.post('/compute/', data)
	print api.get('/compute/')

	print "Ajout d'un flavour"
	data = {
		'name': 'small',
		'vcpu': '1',
		'memory': '512',
		'disk': '4'
	}
	api.post('/flavour/', data)
	print api.get('/flavour/')

	#print "Ajout d'une instance"
	data = {
		'name': 'fubar',
		'desc': 'Instance de teste',
		'flavour': 'small'
	}
	#api.post('/compute/prime/instance/', data)
	#print api.get('/compute/prime/instance/')
