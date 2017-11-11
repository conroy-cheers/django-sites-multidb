from django.conf import settings
from django.contrib.sites.models import Site
from django.apps import apps


# Grab and import the site class to be used
if getattr(settings, 'SITES_MULTIDB_SITE_CLASS', False):
    site_class = apps.get_model(settings.SITES_MULTIDB_SITE_CLASS)
else:
    site_class = Site
