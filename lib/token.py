#-*- coding: utf8 -*-
import uuid
import random

def generate(length=None):
	id = ''

	tmpuuid = uuid.uuid4().hex
	if length is not None:
		if len(tmpuuid) < length:
			while len(tmpuuid) < length:
				tmpuuid += uuid.uuid4().hex
				
		tmpuuid = tmpuuid[:length]
	
	for char in tmpuuid:
		if not char.isdigit():
			if random.randint(0, 2) == 0:
				id += char.upper()
			else:
				id += char
		else:
			id += char
	
	return id
