"""

commands/container.py

description:
	manipulates a container configuration file (container.json) via supplied option arguments

example:
	connect container -e file_name.ext

"""

from json import dumps
from .base_command import BaseCommand

class Container(BaseCommand):
	def run(self):
		from connect.models import Container

		container = Container.load()

		container.path = '../' + container.name

		self.option_commands[self.options['COMMAND']](self, self.options['COMMAND_VALUE'], container)

	def fileInArchive(self, command_value, container):
		container.file_in_archive = command_value
		container.write()

	def format(self, command_value, container):
		container.format = command_value
		container.write()

	def outputFile(self, command_value, container):
		container.output_file = command_value
		container.write()
	
	def useRelationships(self, command_value, container):
		container.use_relationships = bool(command_value)
		container.write()

	def key(self, command_value, container):
		container.key = command_value
		container.write()

	def relationshipsDir(self, command_value, container):
		container.relationships_dir = command_value
		container.write()

	def updateOnly(self, command_value, container):
		container.update_only = bool(command_value)
		container.write()

	def hasAttachments(self, command_value, container):
		container.has_attachments = bool(command_value)
		container.write()

	def view(self, command_value, container):
		container.view = command_value
		container.write()

	def board(self, command_value, container):
		container.board = command_value
		container.write()

	def transform(self, command_value, container):
		container.transform = bool(command_value)
		container.write()

	def geometry(self, command_value, container):
		container.geometry = command_value
		container.write()

	def source(self, command_value, container):
		container.source = command_value
		container.write()

	def source(self, command_value, container):
		container.where_clause = command_value
		container.write()

	option_commands = {
		'file_in_archive' : fileInArchive,
		'format' : format,
		'output_file' : outputFile,
		'use_relationships' : useRelationships,
		'key' : key,
		'relationships_dir' : relationshipsDir,
		'update_only' : updateOnly,
		'has_attachments' : hasAttachments,
		'view' : view,
		'board' : board,
		'transform' : transform,
		'geometry' : geometry,
		'source': source,
		'where_clause': where_clause
	}