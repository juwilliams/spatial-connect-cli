"""

models/data.py

description:
	Data class represents the geojson package in string format for deserlization/serialization from namedtuple

"""
import jsonpickle

from .base_model import BaseModel

class Data(BaseModel):
	def __init__(self, options):
		self.raw_json = ""
		self.type = "{0}.{1}".format(options["type"], options["timestamp"])