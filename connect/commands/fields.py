"""

commands/addfield.py

description:
	adds a mapping field to <connection_name>/fields.json

"""

from .base_command import BaseCommand

class Fields(BaseCommand):
	def run(self):
		from connect.models import Fields		

		#	load fields.json
		fields = Fields.load(self.options)
		fields.path = '.'

		self.option_commands[self.options['COMMAND']](self, self.options['COMMAND_VALUE'] if self.options['COMMAND_VALUE'] else "", fields)

	def add(self, command_value, fields):
		from connect.models import Field

		#	create the field
		field = Field()
		field.field_from = command_value
		field.field_to = self.options['FIELD_TO'] if self.options['FIELD_TO'] else self.options['FIELD_FROM']
		field.type = self.options['FIELD_TYPE'] if self.options['FIELD_TYPE'] else 'text'
		field.length = self.options['FIELD_LENGTH'] if self.options['FIELD_LENGTH'] else '255'

		#	append the new field
		fields.mappings.append(field)

		#	write the output
		fields.write()

	def remove(self, command_value, fields):
		fields.mappings = filter(lambda x: x.field_from != command_value, fields.mappings)

		fields.write()

	def rename(self, command_value, fields):
		for f in fields.mappings:
			if f.field_from == command_value:
				f.field_from == self.options['FIELD_TO']

		fields.write()

	def tag(self, command_value, fields):
		#	find and remove the field
		for f in fields.mappings:
			if f.field_from == command_value:
				if f.tags.find(',') > 0:
					f.tags = ','.join([f.tags, self.options['TAGS']])
				else:
					f.tags = self.options['TAGS']
				break

		fields.write()

	def show(self, command_value, fields):
		for field in fields.mappings:
			print "\r" + field.field_from + " > tags: [" + field.tags + "]"

	option_commands = {
		'add' : add,
		'remove' : remove,
		'tag' : tag,
		'show' : show,
		'rename' : rename
	}

