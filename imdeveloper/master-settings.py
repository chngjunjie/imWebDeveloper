"""
Django settings for imdeveloper project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6r8k#%60ak#gmsz!m8k8q#e*#4o_td+$$dq*s&=)3anm=4c3@4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'homeintro.apps.HomeintroConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'imdeveloper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': '/home/allen/project/online-shop/imWebDeveloper/templates',
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

WSGI_APPLICATION = 'imdeveloper.wsgi.application'



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #      'ENGINE': 'django.db.backends.sqlite3',
    #      'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'wrwrkynm',
    #     'USER': 'wrwrkynm',
    #     'PASSWORD': 'eX148hUqGTMwXjvVwdXZUMuSwLK_RGWD',
    #     'HOST': 'arjuna.db.elephantsql.com',
    #     'PORT': '',
    # }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'online',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static')
]


# DEFAULT_FILE_STORAGE = 'imdeveloper.custom_azure.AzureMediaStorage'
# STATICFILES_STORAGE = 'imdeveloper.custom_azure.PublicAzureStorage'
# #STATIC_ROOT = 'https://allenchngstorage.blob.core.windows.net/lavastatic/'
#
# STATIC_LOCATION = "lavastatic"
#
# AZURE_ACCOUNT_NAME = "allenchngstorage"
# AZURE_CUSTOM_DOMAIN = f'allenchngstorage.blob.core.windows.net'
#
# STATIC_URL = f'https://allenchngstorage.blob.core.windows.net/lavastatic/'
# MEDIA_URL = f'https://allenchngstorage.blob.core.windows.net/lavamedia/'
# MEDIA_ROOT = f'https://allenchngstorage.blob.core.windows.net/lavamedia/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'