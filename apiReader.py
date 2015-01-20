import json
import urllib.request

def jsonRequest(url):
	if url is None:
		return None
    
	response = urllib.request.urlopen(url)
    
	try:
		return json.loads(response.readall().decode('utf-8'))
	except ValueError:
		return None