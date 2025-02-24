






"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

GUARDIAN_RAISE_403 = True
GUARDIAN_RAISE_404 = True

SECURE_SSL_REDIRECT = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'au+me7y%0)7t4b@tqh#r7rez)badj=5vxv#ftyhdpd=a1#r-#d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#TODO: MAKE IT SO THIS TOGGLE IS AUTOMATED FOR DEV/PROD
ALLOWED_HOSTS = ['civam-mt.org', 'http://maps.googleapis.com/', 'https://maps.googleapis.com/']
# STATIC_ROOT = os.path.join('~/CISC475_D5/django_project', 'static/')
STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# UNCOMMENT FOLLOWING 2 LINES FOR LOCAL DEVELOPMENT ONLY!!!!
ALLOWED_HOSTS = ['198.211.99.20', 'localhost:8000', '127.0.0.1', 'civam-mt.org','localhost:4200', "*"]
STATIC_ROOT = os.path.join('~/CIVAM/django_project', 'static/')

# Local Development SMPT Server
# Command to launch: python -m smtpd -n -c DebuggingServer localhost:1025
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 1025

# Gmail SMTP Server
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'civamwebmaster@gmail.com'
EMAIL_HOST_PASSWORD = 'fnanfjjakavwowhk'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

'''
CORS_ORIGIN_WHITELIST = [
    'https://127.0.0.1:4200',
    'http://localhost:4200/',
    'http://localhost:8000/',
    'https://127.0.0.1:8000',
]
'''
CORS_ORIGIN_ALLOW_ALL = True

#SECURE_SSL_REDIRECT = True

# CORS_ALLOWED_ORIGINS = ['http://*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.postgres',
    'guardian',
    'civam.apps.CivamConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'colorfield',
    'adminsortable2',
    'django_countries',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_db',
        'USER': 'django_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = '/static/'
LOGIN_REDIRECT_URL = '/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    
    'my_app.views': {
        'handlers': ['console'],
        'level': 'WARNING',

    },
}

# Countries Settings
# Follows the ISO 3166-1 naming conventions
COUNTRIES_FIRST = [
    'US',
    'UM',
    'CA',
    'UK'
]
