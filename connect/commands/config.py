"""

commands/config.py

description:
	contains global configuration settings for WebEOC and/or ArcGIS

	WebEOC:
		username
		password
		position
		prod_incident
		dev_incident

"""

from json import dumps
from .base_command import BaseCommand

class Config(BaseCommand):
	"""Creating Config"""

	def run(self):
		from connect.models import GlobalConfig

		if self.options['-l']:
			config = GlobalConfig.load()

			if self.options['-c']:
				print '\r\ncontainers > ' + ", ".join(config.containers)
				print '\r\nrunning containers > ' + ", ".join(config.running_containers)
				
			return

		config = GlobalConfig(self.options)

		setup_webeoc = raw_input('Setup WebEOC? [yes/no]: ')
		if setup_webeoc == 'yes' or setup_webeoc == 'y':
			config.webeoc_username = raw_input('WebEOC Username: ')
			config.webeoc_password = raw_input('WebEOC Password: ')
			config.webeoc_position = raw_input('WebEOC Position: ')
			config.webeoc_incident = raw_input('WebEOC Incident: ')
			config.webeoc_jurisdiction = raw_input('WebEOC Jurisdiction: ')

		setup_arcgis = raw_input('Setup ArcGIS [yes/no]: ')
		if setup_arcgis == 'yes' or setup_arcgis == 'y':
			config.arcgis_username = raw_input('ArcGIS Username: ')
			config.arcgis_password = raw_input('ArcGIS Password: ')
			config.arcgis_server = raw_input('ArcGIS Server: ')
			config.arcgis_instance = raw_input('ArcGIS Instance: ')
			config.arcgis_database = raw_input('ArcGIS Database: ')
			config.arcgis_keyword = raw_input('ArcGIS Keyword: ')
			config.arcgis_version = raw_input('ArcGIS Version: ')

		setup_qgis = raw_input('Setup QGIS [yes/no]: ')
		if setup_qgis == 'yes' or setup_qgis == 'y':
			config.qgis_username = raw_input('QGIS Database Username')
			config.qgis_password = raw_input('QGIS Database Password')
			config.qgis_server = raw_input('QGIS Database Server')
			config.qgis_database = raw_input('QGIS Database Name')

		config.write()