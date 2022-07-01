import logging
import random

from django.core.management.base import BaseCommand, CommandParser
from faker import Faker

from apps.humans.models import Human


class Command(BaseCommand):
    help = 'Create humans'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('amount', type=int, )

    def handle(self, *args, **options):
        amount_of_human = options['amount']

        logger = logging.getLogger('create_humans')

        logger.info(f'Amount of users before: {Human.objects.count()}')

        fake = Faker()
        for _ in range(amount_of_human):
            human = Human(
                name=fake.first_name(),
                age=random.randint(0, 150)
            )
            human.save()

        logger.info(f'Amount of users after: {Human.objects.count()}')
