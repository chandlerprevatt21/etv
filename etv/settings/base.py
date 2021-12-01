"""
Django settings for etv project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import environ
import psycopg2
from pathlib import Path
import dj_database_url
import braintree

db_from_env = dj_database_url.config(conn_max_age=500)

env = environ.Env(
    DEBUG=(bool, False)
)

DATABASES = { 'default': dj_database_url.config() }

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
braintree_merchant_id = env('MERCHANT_ID')
braintree_public = env('PUBLIC_KEY')
braintree_private = env('PRIVATE_KEY')
GATEWAY = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Production,
        merchant_id = braintree_merchant_id,
        public_key = braintree_public,
        private_key = braintree_private,
    )
)

SECRET_KEY = env('SECRET_KEY')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_FACEBOOK_KEY = env('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = env('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
MAILCHIMP_API_KEY = env('MAILCHIMP_API_KEY')

AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')

SHIPPO_KEY = env('SHIPPO_KEY')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = 'admin@empowerthevillage.org'
ADMINS = (
    ('Empower The Village', 'admin@empowerthevillage.org'),
)

MANAGERS = ADMINS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1', '127.0.0.1:8000', 'localhost', 'etv.villageblackpages.org', 'www.etv.villageblackpages.org', 'etvlive.herokuapp.com', 'empowerthevillage.org', 'www.empowerthevillage.org', 'etv.empowerthevillage.org']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'accounts',
    'addresses',
    'bfchallenge',
    'billing',
    'carts',
    'content',
    'ckeditor',
    'donations',
    'donors',
    'etv',
    'education',
    'events',
    'health',
    'merchandise',
    'orders',
    'policy',
    'prosperity',
    'phone_field',
    'vbp',
    'social_django',
    'sweetify',
    'storages',
    'whitenoise.runserver_nostatic',
    'ven',
]

AUTH_USER_MODEL = 'accounts.MyUser'

LOGIN_URL = '/login/'
LOGIN_URL_REDIRECT = '/'
LOUGOUT_REDIRECT_URL = 'login'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'etv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(BASE_DIR / 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'etv.context_processors.add_login_form',
            ],
        },
    },
]

SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
)

SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social_django.models.DjangoStorage'
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

WSGI_APPLICATION = 'etv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'd1ttpvr346c994',                     
        'USER': 'pwzmkrllbfxbqg',
        'PASSWORD': '48ad1968c36fe63810a897061cb66a4d3976d01a167292a299def43feaf57b05',
        'HOST': 'ec2-18-215-44-132.compute-1.amazonaws.com',
        'PORT': '5432',                     
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

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
BASE_DIR = (os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# Extra places for collectstatic to find static files.

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_my_proj"),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_QUERYSTRING_AUTH = True

DEFAULT_FILE_STORAGE = 'etv.utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'etv.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'empowerthevillage'
S3DIRECT_REGION = 'us-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = 'https://d1z669787inm16.cloudfront.net/media/'
MEDIA_ROOT = MEDIA_URL
STATIC_URL = 'https://d1z669787inm16.cloudfront.net/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
import datetime


two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
AWS_HEADERS = { 
	'Expires': expires,
	'Cache-Control': 'max-age=%d' % (int(two_months.total_seconds()), ),
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
