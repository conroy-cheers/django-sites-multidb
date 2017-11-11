from django.core.management.base import BaseCommand, CommandError
from django.core import management
from django.conf import settings

from sites_multidb.models import DBConfig


class Command(BaseCommand):
    help = 'Applies migrations to auxiliary site databases.'

    def handle(self, *args, **options):
        # migrate default database
        print("Migrating default database:")
        management.call_command('migrate')
        for db_config in DBConfig.objects.all():
            print("Migrating \"{}\" database:".format(db_config.name))
            # Set database config in settings
            settings.DATABASES[db_config.name] = db_config.as_config_dict()

            management.call_command('migrate', database=db_config.name, noinput=True)
