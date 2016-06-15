"""

commands/register.py

description:
	registers a new container in the global config.json file

"""

from .base_command import BaseCommand

class Register(BaseCommand):
	def run(self):
		from connect.models import GlobalConfig

		config = GlobalConfig.load()

		if not hasattr(config, 'containers'):
			config.containers = []
			
		config.containers.append(self.options['CONNECTION_NAME'])
		config.write()
