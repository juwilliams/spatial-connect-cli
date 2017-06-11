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

	def transform(self):
	#	generates a transform document for the input fields file
		from connect.models import Fields
		from connect.models import Field
		import pkg_resources

		#	load fields.json
		fields = Fields.load(self.options)
		xsl_fields = []
		xsl_output = ''

		resource_package = 'connect';
		transform_path = '/'.join(('templates', 'transform.xsl'))
		transform_field_path = '/'.join(('templates', 'transform_field.xsl'))

		transform_template = pkg_resources.resource_string(resource_package, transform_path)
		transform_field_template = pkg_resources.resource_string(resource_package, transform_field_path)

		for field in fields.mappings:
			xsl_field = transform_field_template.replace('[[FROM_FIELD]]', field.field_from)
			xsl_field = xsl_field.replace('[[TO_FIELD]]', field.field_to)

			xsl_fields.append(xsl_field)

		xsl_output = transform_template.replace('[[FIELDS]]', "\r\n".join(xsl_fields))

		with open('transform.xsl', 'w') as transform_output_file:
			transform_output_file.write(xsl_output)

	option_commands = {
		'webeoc_input' : webeocInput,
		'webeoc_display' : webeocDisplay,
		'transform' : transform
	}

