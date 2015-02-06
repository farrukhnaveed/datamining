# Add specific apps for development server here.
#INSTALLED_APPS += ('debug_toolbar',)

DEBUG = True

# PROJECT DATABASE SETTINGS
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "storedb",
        "USER": "postgres",
        "PASSWORD": "root",
        "HOST": "",
        "PORT": "",
    },
}

# Email settings
DEFAULT_FROM_EMAIL = 'AprioriStore <farrukh.naveed@mezino.com>'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'farrukh.naveed@mezino.com'
EMAIL_HOST_PASSWORD = '2tomato2'
EMAIL_USE_TLS = True 
EMAIL_PORT = 587
