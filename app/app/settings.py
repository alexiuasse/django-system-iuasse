"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pg8s7wu@=v9ei^eqyum$k@i4oh2%k2jvrt!rj*6ddoyb#j_3au'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '0.0.0.0']

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django_cleanup.apps.CleanupConfig',
    # 'corsheaders',
    'bootstrap5',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_tables2',
    'django_filters',
    'app',
    'financial',
    'service',
    'client',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # activate translation
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'app.context_processors.general_template_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'
LANGUAGES = [
    ('en', 'English'),
    ('pt-br', 'Brazilian Portuguese'),
]
LOCALE_PATHS = (BASE_DIR / 'locale',)

TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = '/dashboard/'

# Custom settings

VERSION = "v1.0.0+0a"

NAME_OF_ENTERPRISE = "Iuasse System"
NAME_OF_ENTERPRISE_SHORT = "Iuasse System"
FOOTER_LINK = "https://www.iuasse.com"
FOOTER_TEXT = "Iuasse, Serviços Digitais"
FOOTER_COPYRIGHT = "Copyright © 2021"
CONTACT_EMAIL = "alexiuasse@gmail.com"
SOURCE_CODE_LINK = "https://github.com/alexiuasse/django-system-iuasse"

MONEY_SYMBOL = "R$"
CHART_MONTHS_LABELS = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai',
                       'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']

DEFAULT_DECIMAL_PLACES = 2
DEFAULT_MAX_DIGITS = 11

# Django tables 2
DJANGO_TABLES2_TEMPLATE = "django_tables2/bootstrap4.html"

# Django Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
