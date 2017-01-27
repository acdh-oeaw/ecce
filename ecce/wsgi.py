"""
WSGI config for ted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""


import os
import sys

sys.path.append('/var/www/html')
sys.path.append('/var/www/html/myenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] =  "ecce.settings.server"

application = get_wsgi_application()

