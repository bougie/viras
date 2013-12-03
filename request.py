#-*- coding: utf8 -*-
import requests
import hashlib
import time
import json

class Api:
	def __init__(self, root, applicationKey, applicationSecret, consumerKey = ""):
		self.baseUrl = root
		self.applicationKey = applicationKey
		self.applicationSecret = applicationSecret
		self.consumerKey = consumerKey
		
	def get(self, path):
		return self.rawCall("get", path)
    
	def put(self, path, content):
		return self.rawCall("put", path, content)
    
	def post(self, path, content):
		return self.rawCall("post", path, content)
    
	def delete(self, path, content = None):
		return self.rawCall("delete", path, content)
		
	def rawCall(self, method, path, content = None):
		targetUrl = self.baseUrl + path

		body = ""
		if content is not None:
			body = json.dumps(content)
			
		s1 = hashlib.sha1()
		s1.update("+".join([
			self.applicationSecret,
			self.consumerKey,
			body
		]))
		sig = "$1$" + s1.hexdigest()
		queryHeaders = {
			"X-Viras-Application": self.applicationKey,
			"X-Viras-Consumer": self.consumerKey,
			"X-Viras-Signature": sig
		}

		if self.consumerKey == "":
			queryHeaders = {
				"X-Viras-Application": self.applicationKey,
			}
		req = getattr(requests, method.lower())

		result = req(targetUrl, headers=queryHeaders, data=body).text
        
		return json.loads(result)
		
	def requestConsumerKey(self, login, password):
		targetUrl = self.baseUrl + "/auth"
		
		queryData = {
			'login': login,
			'password': password
		}
        
		q = requests.post(
			targetUrl,
			headers = {
				"X-Viras-Application": self.applicationKey,
				"X-Viras-Secret": self.applicationSecret
			},
			data = queryData
		)
        
		return json.loads(q.text)

