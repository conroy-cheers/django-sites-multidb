from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.conf import settings

from sites_multidb.models import DBConfig


class Command(BaseCommand):
    help = 'Creates a superuser for the specified domain.'

    def add_arguments(self, parser):
        parser.add_argument('domain')

    def handle(self, *args, **options):
        # Set database config in settings
        db_config = DBConfig.objects.get(name=options['domain'])
        settings.DATABASES[db_config.name] = db_config.as_config_dict()

        management.call_command('createsuperuser', database=db_config.name)
