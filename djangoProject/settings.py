"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from os.path import dirname
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.core.checks import templates
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY'),
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



DEFAULT_EMAIL = ''
EMAIL_PASSWORD = ''

#DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_EMAIL")
DEFAULT_FROM_EMAIL = DEFAULT_EMAIL

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.Email SITE_URL Backend'
# MAILER_EMAIL_BACKEND = EMAIL_BACKEND

try:
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
    # EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    EMAIL_HOST_PASSWORD = EMAIL_PASSWORD
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
except:
    pass

SITE_URL = ""
if DEBUG:
    SITE_URL = "http://127.0.0.1:8000"






# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'cart',
    'orders',
    'accounts',
    'marketing',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'marketing.middleware.DisplayMarketing', #customized middleware
]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'djangoProject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

#####################################################################################

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
MARKETING_HOUR_OFFSET = 1
MARKETING_SECOND_OFFSET = 8

###################################################################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static","static_root")


MEDIA_ROOT = BASE_DIR/"media/"

# print(MEDIA_ROOT)
# MEDIA_ROOT = "static/media"
STATIC_ROOT = "static/static_root"
STATICFILES_DIRS = (
    BASE_DIR / "static/static_files",
)
# print(MEDIA_URL)
# collectstatic collect static files from static file folder to static root folder

###################################################################################
#HIDE SECRET KEY
# STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")  #SERVER SIDE
# STRIPE_PUBLISHABLE_KEY = os.environ.get("STRIPE_PUBLISHABLE_KEY")  #CLIENT SIDE

STRIPE_SECRET_KEY = ''
STRIPE_PUBLISHABLE_KEY = ''