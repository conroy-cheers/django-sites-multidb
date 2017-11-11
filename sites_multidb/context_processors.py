from .utils import site_class


def site(request):
    return {
        'site': site_class.objects.get_current()
    }
