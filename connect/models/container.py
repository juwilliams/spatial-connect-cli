"""

models/container.py

description:
	Container Class which defines everything needed for SpatialConnect to retrieve or push data

"""
import jsonpickle

from .base_model import BaseModel
from .field import Fields

class Container(BaseModel):
	def __init__(self, options):
		#	argument mapping
		self.name = options['CONNECTION_NAME']
		self.destination = options['DESTINATION'] if options['DESTINATION'] else ''
		self.source = options['SOURCE']
		self.transform = options['-t']
		self.format = options['FORMAT']
		self.type = 'container'
		self.license_type = 'DESKTOP_BASIC'
		self.source_username = ''
		self.source_password = ''
		self.board = ''
		self.view = ''
		self.geometry = ''
		self.file_in_archive = ''
		self.output_file = ''
		self.where_clause = ''
		self.wkid = int(options['WKID']) if options['WKID'] else 4326
		self.use_relationships = options['-r'] if options['-r'] else False
		self.key = options['KEY'] if options['KEY'] else 'id'
		self.update_only = False
		self.has_attachments = False

		#	directory creation
		self.path = self.name
		self.push_dir = self.path + '/push'
		self.pull_dir = self.path + '/pull'
		self.temp_dir = self.path + '/temp'
		self.relationships_dir = self.name

	def build(self):
		#	create required directories
		self.createDir(self.path)
		self.createDir(self.push_dir)
		self.createDir(self.pull_dir)
		self.createDir(self.pull_dir + '/archive')
		self.createDir(self.temp_dir)

		#	create history file to store uids that have been captured
		self.createFile(self.path + '/relationships.json', '{"keys" : []}')
		self.createFile(self.pull_dir + '/history.json', '{"uids" : []}')
		self.createFile(self.push_dir + '/history.json', '{"uids" : []}')

		#	create and write fields.json, where fields are added and removed
		fields = Fields(self.path + '/')
		fields.write()

	def rebuild(self):
		self.path = '.'
		self.push_dir = self.path + '/push'
		self.pull_dir = self.path + '/pull'
		self.temp_dir = self.path + '/temp'

		self.removeDir(self.push_dir)
		self.removeDir(self.pull_dir)
		self.removeDir(self.temp_dir)

		#	create required directories
		self.createDir(self.push_dir)
		self.createDir(self.pull_dir)
		self.createDir(self.pull_dir + '/archive')
		self.createDir(self.temp_dir)

		#	create history file to store uids that have been captured
		self.createFile(self.path + '/relationships.json', '{"keys" : []}')
		self.createFile(self.pull_dir + '/history.json', '{"uids" : []}')
		self.createFile(self.push_dir + '/history.json', '{"uids" : []}')

	@staticmethod
	def load():
		return jsonpickle.decode(Container.openFile('container.json'))

	@staticmethod
	def openFile(file_name):
		with open(file_name, 'r') as outfile:
			data = outfile.read()
			return data

