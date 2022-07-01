from django.core.management.base import BaseCommand, CommandParser

from apps.password_generator.services import generate_password


class Command(BaseCommand):
    help = 'Generate password'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('length', type=int, )

    def handle(self, *args, **options):
        print(generate_password(password_length=options['length']))
