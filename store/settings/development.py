import os
# Add specific apps for development server here.
#INSTALLED_APPS += ('debug_toolbar',)

DEBUG = True

# PROJECT DATABASE SETTINGS
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "storedb3",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "",
        "PORT": "",
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}

# Email settings
DEFAULT_FROM_EMAIL = 'AprioriStore <dummy@domain.com>'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dummy@domain.com'
EMAIL_HOST_PASSWORD = '123456'
EMAIL_USE_TLS = True 
EMAIL_PORT = 587

os.system('clear')
