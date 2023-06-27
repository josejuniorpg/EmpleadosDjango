# SECURITY WARNING: don't run with debug turned on in production!
import os.path
#from django.conf import settings

from .base import *
from io import FileIO

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [ # Aplicaciones instaladas. Y tambien paquetes.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Local Apps
    'applications.empleados', #En django, las rutas son con . y no con /
    'applications.departamento',
    'applications.home',
    # Third Apps
    'ckeditor',
]

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'yuni',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
#todo Ver que en linux y Mac no de error de rutas al cargar static
STATICFILES_DIRS = [(BASE_DIR/'static')]
print('lA RUTA',STATICFILES_DIRS)