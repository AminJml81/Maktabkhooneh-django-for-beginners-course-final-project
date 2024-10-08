"""
Django settings for core project.
Generated by 'django-admin startproject' using Django 4.2.13.
"""

# DEVELOPMENT SETTINGS are in the dev.py(hardcoded)
# DEPLOYMENT SETTINGS are in the prod.py
# COMMON SETTINGS are here

from pathlib import Path
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Application definition

INSTALLED_APPS = [
    # captcha related apps
    'captcha',
    "multi_captcha_admin",
    'django_recaptcha',

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # humanize
    "django.contrib.humanize",

    # allauth 
    'allauth',
    'allauth.account',

    # sites
    "django.contrib.sites",

    # sitesmap
    "django.contrib.sitemaps",

    # robots
    "robots",

    # taggit
    "taggit",
    
    # tinymce
    'tinymce',
    
    #local apps
    "blog.apps.BlogConfig",
    "website.apps.WebsiteConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # allauth
    "allauth.account.middleware.AccountMiddleware",

]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"
MEDIA_URL = 'media/' 

STATIC_ROOT = BASE_DIR/'static'
MEDIA_ROOT = BASE_DIR/'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]


# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# recaptcha settings
# MULTI_CAPTCHA_ADMIN = {
#     'engine': 'simple-captcha',
# }
MULTI_CAPTCHA_ADMIN = {
    'engine': 'recaptcha',
}

RECAPTCHA_PRIVATE_KEY = config('RECAPTCHA_PRIVATE_KEY')
RECAPTCHA_PUBLIC_KEY = config('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_REQUIRED_SCORE = config('RECAPTCHA_REQUIRED_SCORE', cast=float)

# sites setting
SITE_ID = config("SITE_ID", cast=int)

# taggit
TAGGIT_CASE_INSENSITIVE = True

# allauth settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True

LOGIN_REDIRECT_URL='/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_SIGNUP_REDIRECT_URL = '/'


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = config('USER_EMAIL')
EMAIL_HOST_PASSWORD = config('USER_PASSWORD')
