"""

models/field.py

description:
	field mapping for incoming/outgoing data between systems

	from_field > input data
	to_field > output data

"""

import jsonpickle

from .base_model import BaseModel

class Fields(BaseModel):
	def __init__(self, path):
		self.mappings = []
		self.type = 'fields'
		self.path = path		

	@staticmethod
	def load(options):
		return jsonpickle.decode(Fields.openFile('fields.json'))

	@staticmethod
	def openFile(file_name):
		with open(file_name, 'r') as outfile:
			data = outfile.read()
			return data

class Field(BaseModel):
	def __init__(self):
		self.field_from = ''
		self.field_to = ''
		self.tags = ''
