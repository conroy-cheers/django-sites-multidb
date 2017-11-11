from django.apps import apps
from django.db import connections

from .models import DBConfig
from .utils import site_class


def get_db_config(site):
    """
    Gets the appropriate DBConfig for a Site, using the site's 'db_config' relation if defined, or otherwise by finding 
    the DBConfig with name matching the Site's.
    :param site: Site or subclass instance
    :return: DBConfig instance
    """
    if hasattr(site, 'db_config') and type(site.db_config) is DBConfig:
        return site.db_config
    else:
        try:
            return DBConfig.objects.get(name=site.domain)
        except DBConfig.DoesNotExist:
            return None


class MultiDBRouter:
    """
    A router to read and write to the DB matching the current Site's name. 
    """

    def db_for_read(self, model, **hints):
        # Check for default DB flag
        if getattr(model, 'SITES_MULTIDB_USE_DEFAULT_DB', False) is True:
            return 'default'

        current_site = site_class.objects.get_current()
        if current_site.name in connections.databases:
            return current_site.name
        else:
            current_db_config = get_db_config(current_site)
            if current_db_config:
                # Add the database config to connections
                connections.databases[current_site.name] = current_db_config.as_config_dict()
                return current_site.name
        return None

    def db_for_write(self, model, **hints):
        # Check for default DB flag
        if getattr(model, 'SITES_MULTIDB_USE_DEFAULT_DB', False) is True:
            return 'default'

        current_site = site_class.objects.get_current()
        if current_site.name in connections.databases:
            return current_site.name
        else:
            current_db_config = get_db_config(current_site)
            if current_db_config:
                # Add the database config to connections
                connections.databases[current_site.name] = current_db_config.as_config_dict()
                return current_site.name
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name is None:
            # not a model - we don't care
            return None
        model = apps.get_model(app_label, model_name)
        if getattr(model, 'SITES_MULTIDB_USE_DEFAULT_DB', False) is True:
            # this model is for default db only
            return db == 'default'
        return None
