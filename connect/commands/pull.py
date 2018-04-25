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
		from connect.util import data

		config = GlobalConfig.load()

		try:
			# iterate over the registered containers and pull data for each
			for container_name in config.containers:
				container = Container.load(container_name)
				
				# register the container as running
				config.running_containers.append(container_name)
				config.write()

				fetchedObj = data.fetchJsonAsObj(container.source)

				for feature in fetchedObj.features:
					print feature.geometry.coordinates
		except Exception as e:
			# clean out the running containers
			print "error encountered while fetching data, see error log for details"

			# throw the error up to the global cli error handler
			raise e
		finally:
			config.running_containers = []
			config.write()

