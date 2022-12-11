from core.settings import *

ALLOWED_HOSTS = []

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'QuizApp',
        'PASSWORD': '1',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}