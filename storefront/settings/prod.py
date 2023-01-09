import os
from .common import *
import dj_database_url



DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ["jiahongbuy-prod.herokuapp.com"]

DATABASES = {
    'default': dj_database_url.config() 
}
REDIS_URL = os.environ['REDIS_URL']
CELERY_BROKER_URL = REDIS_URL
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}