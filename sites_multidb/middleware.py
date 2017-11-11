from django.conf import settings
from django.contrib.sites.models import Site
from django.http import HttpResponseNotFound

from .utils import site_class

HOST_CACHE = {}


class DynamicSiteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def _get_site(request):
        host = request.get_host()
        shost = host.rsplit(':', 1)[0]  # Host without port

        try:
            # Check cache first
            return HOST_CACHE[host]
        except KeyError:
            pass

        try:
            # Check DB
            site = site_class.objects.get(domain=host)
            HOST_CACHE[host] = site
            return site
        except Site.DoesNotExist:
            pass

        if shost != host:
            # Check DB for host without port
            try:
                site = site_class.objects.get(domain=shost)
                HOST_CACHE[host] = site
                return site
            except Site.DoesNotExist:
                pass

        return None

    def __call__(self, request):
        site = self._get_site(request)
        if site:
            settings.SITE_ID.set(site.pk)
            request.subdomain = site
        else:
            # No matching site
            return HttpResponseNotFound()

        response = self.get_response(request)
        return response
