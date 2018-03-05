from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(%wts-t(pgg5(%dd42dghc=)(/&%y@)w15s6b-e8)dddsedxxcv432$d8$e3x7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eccedev',
        'USER': 'eccedev',
        'PASSWORD': 'lU011F8huZjr',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
# start server "pg_ctl" -D "ecce" -l logfile start
