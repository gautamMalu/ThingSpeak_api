import requests

class channel:

	"""
	This a class for channels on thinkspeak.com. ThingSpeak is awesome
	
	"""

	def __init__(self,id):
		self.id = id

	def getfeeds(self,results=10,median="daily",api_key=""):
		"""
		It returns live feeds of channel in json format.
		Attributes:
		api_key (string) Read API Key for this specific Channel (optional--no key required for public channels)
		results (integer) Number of entries to retrieve, 8000 max, default of 100 (optional)
		median (integer or string) Get median of this many minutes, valid values: 10, 15, 20, 30, 60, 240, 720, 1440, "daily" (optional)

		"""


		url = "http://api.thingspeak.com/channels/"+str(self.id)+"/feeds.json"
		params = {'results': results, 'median': median}
		# Add api_key also to the request if provided
		if api_key:
			params['key'] = api_key
		r = requests.get(url,params=params)

		if r.status_code == 400:
				print "It's private channel please provide correct api_key"

		r.raise_for_status()
		return r.content


	def getlastEntry(self,api_key=""):
		"""
		To get the last entry in the Channel feed

		Attributes:
		api_key (string) Read API Key for this specific Channel (optional--no key required for public channels)
		"""
		url = "http://api.thingspeak.com/channels/"+str(self.id)+"/feeds/last"+".json"
		params = {}
		if api_key:
			params['key'] = api_key
		r = requests.get(url,params=params)

		if r.status_code == 400:
				print "It's private channel please provide correct api_key"

		r.raise_for_status()
		return r.content





	def getfeeds_field(self,field=1,results=10,api_key=""):
		url = "http://api.thingspeak.com/channels/"+str(self.id)+"/field/"+str(field)+".json"
		params = {'results': results}
		# Add api_key also to the request if provided
		if api_key:
			params['key'] = api_key
		r = requests.get(url,params=params)
		#print r.url
		if r.status_code == 400:
				print "It's private channel please provide correct api_key"

		r.raise_for_status()
		return r.content


	def updatefeeds(self,value,field_id="field1",api_key=""):
		"""
		Update the feeds of a field
		Attributes:
		value = value to updated
		field_id="field1" or "field2"
		api_key = write_api_key
		"""

		if not api_key:
			print "please pass api_key='write_api_key'"
		else:
			url = "https://api.thingspeak.com/update"
			params = {'key':api_key,field_id:value}

			r = requests.post(url,params=params)
		#	print r.url
		if r.status_code == 400:
				print "Please provide correct api_key"

		r.raise_for_status()
