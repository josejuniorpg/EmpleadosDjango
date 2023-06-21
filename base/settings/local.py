# SECURITY WARNING: don't run with debug turned on in production!
from .base import *

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
    'applications.empleado', #En django, las rutas son con . y no con /
    'applications.departamento',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'