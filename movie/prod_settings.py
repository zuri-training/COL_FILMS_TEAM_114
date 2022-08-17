""" Production Settings """
# default: use settings from main settings.py if not overwritten
from .settings import *

import django_heroku
from decouple import config, Csv

DEBUG = False
# DEBUG = config('DEBUG')
SECRET_KEY = config('SECRET_KEY')

# adjust to the URL of your Heroku app
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# Activate Django-Heroku.
django_heroku.settings(locals())