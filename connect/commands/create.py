"""

commands/create.py

description:
	creates and builds all configuration files and directories for a new container

example:
	./container_name/container.json     contains configuration settings required to process and collect/push data for a container
	./container_name/push               contains DATE_push.json files which describe data pushed from the source
	./container_name/pull				contains DATE_pull.json files which describe data pulled from the source

"""

from json import dumps, loads
from .base_command import BaseCommand

class Create(BaseCommand):
	def run(self):
		from connect.models import Container

		print '\r\nCreating new container > ' + self.options['CONNECTION_NAME']
		
		container = Container(self.options)

		#	build directory structure for this container
		container.build()

		#	serialize this container and output it to container.json
		container.write()

		print '\r\nCreate container done >\r\n' + dumps(loads(container.json), indent=4, sort_keys=True) + '\r\n'