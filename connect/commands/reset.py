"""

commands/reset.py

description:
	resets parameters for a container or configuration

example:
	./container_name/container.json     contains configuration settings required to process and collect/push data for a container
	

"""

from json import dumps
from .base_command import BaseCommand

class Reset(BaseCommand):
	def run(self):
		self.option_commands[self.options['COMMAND']](self, self.options['COMMAND_VALUE'])

	# clears out history.json, relationships.json and moves all 
	# DATE_pull.json files to the archive sub directory
	def resetContainer(self, command_value):
		from connect.models import Container

		container = Container.load()

		container.rebuild()

		container.write()

	def resetRunning(self, command_value):
		from connect.models import GlobalConfig

		config = GlobalConfig.load()
		
		config.running_containers = []

		config.write()

	# command to handler mappings
	option_commands = {
		'container' : resetContainer,
		'running' : resetRunning
	}