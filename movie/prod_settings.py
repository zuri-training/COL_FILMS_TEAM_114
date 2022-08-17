""" Production Settings """
# default: use settings from main settings.py if not overwritten
from .settings import *

import django_heroku
from decouple import config, Csv


DEBUG = config('DEBUG')
SECRET_KEY = config('SECRET_KEY')


from decouple import config
# DEBUG = config('DEBUG')

DEBUG = False
SECRET_KEY = config('SECRET_KEY')

# adjust to the URL of your Heroku app
ALLOWED_HOSTS = config('ALLOWED_HOSTS')

# Activate Django-Heroku.
django_heroku.settings(locals())