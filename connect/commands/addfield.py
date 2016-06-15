"""

commands/addfield.py

description:
	adds a mapping field to <connection_name>/fields.json

"""

from .base_command import BaseCommand

class AddField(BaseCommand):
	def run(self):
		from connect.models import Fields
		from connect.models import Field

		#	load fields.json
		fields = Fields.load(self.options)

		fields.path = '.'

		#	create the field
		field = Field()
		field.field_from = self.options['FIELD_FROM']
		field.field_to = self.options['FIELD_TO'] if self.options['FIELD_TO'] else self.options['FIELD_FROM']
		field.type = self.options['FIELD_TYPE'] if self.options['FIELD_TYPE'] else 'text'
		field.length = self.options['FIELD_LENGTH'] if self.options['FIELD_LENGTH'] else '255'

		#	append the new field
		fields.mappings.append(field)

		#	write the output
		fields.write()

