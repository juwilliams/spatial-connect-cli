"""

commands/removefield.py

description:
	removes a mapping field from <connection_name>/fields.json

"""

from .base_command import BaseCommand

class AddField(BaseCommand):
	def run(self):
		from connect.models import Fields
		from connect.models import Field

		#	load fields.json
		fields = Fields.load(self.options)

		#	determine if mappings exists
		if not hasattr(fields, 'mappings'):
			print 'Mappings not present in fields.json. Aborting!'
			return

		#	find and remove the field
		for f in fields.mappings:
			if f.field_from == self.options['FIELD_FROM'] and f.field_to == self.options['FIELD_TO'] if self.options['FIELD_TO'] else self.options['FIELD_FROM']:
				fields.mappings.remove(f)
				break

		#	write the output
		fields.write()

