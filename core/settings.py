"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, sys
from django.utils.translation import gettext_lazy as _

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-g$r%p8=*y8i9vaj2y395i435!rymb3t##8snyqz-q7e_fk8&li"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.sites",
    # custom apps
    "manager.apps.ManagerConfig",
    "supplier.apps.SupplierConfig",
    "buyer.apps.BuyerConfig",
    "payment.apps.PaymentConfig",
    "auth_app.apps.AuthAppConfig",
    "app_admin.apps.AppAdminConfig",
    "admin_api.apps.AdminApiConfig",
    "api.apps.ApiConfig",
    # third party
    "rest_framework",
    "channels",
    "rosetta",
    "django_user_agents",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.linkedin",
]

# django_user_agents

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '127.0.0.1:11211',
#     }
# }

USER_AGENTS_CACHE = "default"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # translations
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_user_agents.middleware.UserAgentMiddleware",
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

ROOT_URLCONF = "core.urls"

USE_I18N = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "manager.context_processors.categories_showroows",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"
# ASGI APP FOR CHANNELS
ASGI_APPLICATION = "core.routing.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
        "hosts": [("127.0.0.1", 6379)],
        },
    },
    # "ROUTING": "core.routing.channel_routing",
    #"default": {
    #    "BACKEND": "channels.layers.InMemoryChannelLayer",
    #},
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.postgresql_psycopg2",
         "NAME": "tradeoasis",
         "USER": "tradeoasis",
         "PASSWORD": "tradeoasis",
         "HOST": "localhost",
         "PORT": "",
     }
    #"default": {
    #    "ENGINE": "django.db.backends.sqlite3",
    #    "NAME": BASE_DIR / "db.sqlite3",
    #}
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# STATIC_ROOT = 'static'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "auth_app.User"


# django debug toolbar
INTERNAL_IPS = [
    "127.0.0.1",
]


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "phillipmugisa4@gmail.com"
EMAIL_HOST_PASSWORD = "xkeagmjrhlcwlanb"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "phillipmugisa4@gmail.com"

LOGIN_REDIRECT = "/auth/login/"
LOGIN_URL = "/auth/login/"

CORS_ALLOW_ALL_ORIGINS = True
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ]
}
CORS_URLS_REGEX = r"^/api/.*$"

# translations
LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", _("English")),
    ("ar", _("Arabic")),
    ("fr", _("French")),
    ("de", _("German")),
)

SITE_ROOT = os.path.dirname(os.path.realpath(__name__))
LOCALE_PATHS = (os.path.join(SITE_ROOT, "locale"),)

MODELTRANSLATION_DEFAULT_LANGUAGE = "en"
MODELTRANSLATION_LANGUAGES = ("ar", "fr", "de", "en")

# PAYMENTS
# braintee
# if (len(sys.argv) >= 2 and sys.argv[1] == 'runserver'):
#     BRAINTREE_PRODUCTION = False
# else:
BRAINTREE_PRODUCTION = False
BRAINTREE_MERCHANT_ID = "zq9jqbg246n5zjt6"
BRAINTREE_PUBLIC_KEY = "4spv6wdb3xqwbvv4"
BRAINTREE_PRIVATE_KEY = "4fa06482b576443eaaba4021d89cb9c0"


# allauth
SITE_ID = 1
# Provider specific settings
SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "linkedin": {
        "SCOPE": ["r_basicprofile", "r_emailaddress"],
        "PROFILE_FIELDS": [
            "id",
            "first-name",
            "last-name",
            "email-address",
            "picture-url",
            "public-profile-url",
        ],
    },
}

# ACCOUNT_SIGNUP_FORM_CLASS = 'auth_app.forms.CustomSignupForm'
ACCOUNT_FORMS = {
    # "signup": "allauth.account.forms.SignupForm",
    # 'signup': 'auth_app.forms.CustomSignupForm',
}

ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_AUTO_SIGNUP = False
ACCOUNT_SIGNUP_REDIRECT_URL = reverse_lazy("auth_app:business")


# custom
CHATROOMFILES_DIR = os.path.join(BASE_DIR, "chatrooms")
