"""

commands/unregister.py

description:
	unregisters a container from the global config

"""

from .base_command import BaseCommand

class Unregister(BaseCommand):
	def run(self):
		from connect.models import GlobalConfig

		config = GlobalConfig.load()

		if not hasattr(config, 'containers'):
			print 'Configuration has no containers'
			return
			
		config.containers.remove(self.options['CONNECTION_NAME'])
		config.write()
