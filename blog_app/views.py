import logging
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView

logger = logging.getLogger('blog.views')

# blog_app views file
# Create your views here.
def global_setting(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'SITE_DESC': settings.SITE_DESC,
    }

class HomePage(TemplateView):
    try:
        pass
    except Exception as e:
        logger.error(e)
    template_name = 'index.html'