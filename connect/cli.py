"""
usage:
	connect -h | --help
	connect create CONNECTION_NAME -d DESTINATION -s SOURCE -f FORMAT -g GEOMETRY [-t] [-w WKID] [-r] [-k KEY]
	connect create CONNECTION_NAME --dest=DESTINATION --source=SOURCE --format=FORMAT --geometry=GEOMETRY [-t] [--wkid=WKID] [-r] [--key=KEY]
	connect container COMMAND [COMMAND_VALUE]
	connect config
	connect register CONNECTION_NAME
	connect unregister CONNECTION_NAME
	connect addfield FIELD_FROM [FIELD_TO] [FIELD_TYPE] [FIELD_LENGTH]
	connect removefield FIELD_FROM
	connect generate FORMAT
	connect reset COMMAND [COMMAND_VALUE]

arguments:
	CONNECTION_NAME      Name of the new container
	DESTINATION          Target System (WebEOC | ArcGIS) - Push Configuration
	SOURCE               Source System (WebEOC | ArcGIS) - Pull Configuration
	FORMAT               Response format from data source (See format section below)
	GEOMETRY             Geometry type (point, polygon, line, polyline)
	FIELD_FROM           Data field as described in data source
	FIELD_TO             Data field as preferred in target system, defaults to FIELD_FROM if not supplied
	FIELD_TYPE           Data field data type (default: text)
	FIELD_LENGTH         Data field data length (default: 255)
	KEY                  Key field used for relationships (default: id)
	WKID                 ArcGIS featureclass WKID (default: 4326)
	COMMAND              Sub-command (see values below)

options:
  	-h, --help                                      Show this screen. 
  	-v, --version                                   Show version. 
  	-n CONNECTION_NAME --name=CONNECTION_NAME       Container Name 
  	-g GEOMETRY --geometry=GEOMETRY                 Geometry type (point, polygon, line, polyline)
  	-d DESTINATION --dest=DESTINATION               Target System (WebEOC | ArcGIS) - Push Configuration 
  	-s SOURCE --source=SOURCE                       Source System (WebEOC | ArcGIS) - Pull Configuration 
	-f FORMAT --format=FORMAT                       Response format from data source 
	-k KEY --key=KEY                                Key field used for relationships
	-t                                              Transform response
	-w, --wkid                                      ArcGIS featureclass WKID (default: 4326)
	-e, --extract                                   File in archive to extract
	-r                                              Use relationships (maintains id and external id so updates are possible)

examples:
  	connect create -n MyContainer -d WebEOC -f Features -t -i 15
  	connect create --name MyContainer --source WebEOC --format Features -t -i 15
  	connect config

formats:
	arcgis               Data sourced from ArcGIS in features
	webeoc               Data sourced from Intermedix WebEOC API in xml
	webeoc_input         HTML generation for Intermedix Input View
	webeoc_display       HTML generation for Intermedix Display View

sub-commands:
	container                                     Used in reset command. Rebuilds history.json, relationships.json and purges push/pull sub directories
	container file_in_archive                     Modifies the file_in_archive field in container.json
	container format                              Modifies the format field in container.json
	container output_file                         Modifies the output_file field in container.json
	container key                                 Modifies the key field in container.json
	container relationships_dir                   Modifies the relationships_dir field in container.json
	container update_only                         Modifies the update_only field in container.json
	container has_attachments                     Modifies the has_attachments field in container.json
	container transform 						  Modifies the transform field in container.json
	running                                       Used in reset command. Clears the running_containers property in config.json.

help:
  	For help using this tool, please open an issue on the Github repository:
  	https://github.com/juwilliams/spatial-connect-cli
"""

from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION

def main():
	"""Main CLI Entrypoint"""
	import commands
	from commands import BaseCommand

	options = docopt(__doc__, version=VERSION)

	# iterate over registered commands and attempt to find one matching the user input
	for k, v in options.iteritems():
		if hasattr(commands, k) and v:
			module = getattr(commands, k)
			commands = getmembers(module, isclass)
			command = [command[1] for command in commands if command[0] != 'BaseCommand'][0]
			command = command(options)
			command.run()
