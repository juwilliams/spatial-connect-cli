"""
commands/pull.py

description:
	processes registered containers, downloading data from the specified source and producing geoJSON packages for
	later distribution via the push command

usage:
	create a container with the 'connect create' command and then register it with the 'connect register' command

	once you have a registered container execute the 'connect pull' command
"""

from json import dumps, loads
from .base_command import BaseCommand

class Pull(BaseCommand):
	def run(self):
		from connect.models import GlobalConfig
		from connect.models import Container
		from connect.models import Field

		config = GlobalConfig.load()

		# iterate over the registered containers and pull data for each
		for container_name in config.containers:
			container = Container.load(container_name)
			container.serialize()
			
			print '\r\nContainer config >\r\n' + dumps(loads(container.json), indent=4, sort_keys=True) + '\r\n'