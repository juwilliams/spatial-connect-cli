"""
commands/generate.py

description:
	generates output files for miscellaneous use cases

	these are generally helper functions that produce some beneficial or time saving output

usage:
	register a method in the option_commands dictionary and define a matching method
	to process something and generate the output
"""

from json import dumps
from .base_command import BaseCommand

class Generate(BaseCommand):
	def run(self):	
		self.option_commands[self.options['FORMAT']](self)

	def webeocInput(self):
		pattern = '<span>\n\r\t<label>{0}</label>\n\r\t<input type="text" name="{0}" />\n\r</span>\n\r'
		output = self.getOutputFormat(pattern)

		print output

	def webeocDisplay(self):
		header_pattern = '<th>{0}</th>\n\r'
		cell_pattern = '<td>\n\r\t<eocfield name="{0}"></eocfield>\n\r</td>\n\r'
		
		output = '<-- HEADERS -->\n\r'
		output = output + self.getOutputFormat(header_pattern)
		output = output + '<-- CELLS -->\n\r'
		output = output + self.getOutputFormat(cell_pattern)

		print output

	#	generates an output format based on container fields.json
	def getOutputFormat(self, type_pattern):
		from connect.models import Fields
		from connect.models import Field

		output = ''

		#	load fields.json
		fields = Fields.load(self.options)

		#	generate output html
		for m in fields.mappings:
			output = output + type_pattern.format(m.field_to)

		return output

	option_commands = {
		'webeoc_input' : webeocInput,
		'webeoc_display' : webeocDisplay
	}

