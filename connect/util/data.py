from collections import namedtuple
from json import loads

def fetchJsonAsObj(url):
	from urllib2 import urlopen
	
	response = urlopen(url)
	data = response.read()

	if data is not None:
		return json2obj(data)
	else:
		return data

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return loads(data, object_hook=_json_object_hook)