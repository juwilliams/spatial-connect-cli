"""

models/config.py

description:
	The global config model contains connection parameters for WebEOC and ArcGIS

"""

import jsonpickle

from .base_model import BaseModel


class GlobalConfig(BaseModel):
	def __init__(self, options):
		#	misc fields
		self.type = 'config'
		self.path = '.'
		self.json = ''
		self.running_containers = []
	
	@staticmethod
	def load():
		return jsonpickle.decode(GlobalConfig.openFile('config.json'))

	@staticmethod
	def openFile(file_name):
		with open(file_name, 'r') as outfile:
			data = outfile.read()
			return data