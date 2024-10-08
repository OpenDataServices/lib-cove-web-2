# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import environ
from django.utils.crypto import get_random_string

COVE_CONFIG = {
    "app_name": "test",
    "app_base_template": "libcoveweb2/base.html",
    "input_methods": ["upload", "url", "text"],
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)"
secret_key = get_random_string(50, chars)

env = environ.Env(  # set default values and casting
    DEBUG=(bool, True),
    PIWIK_URL=(str, ""),
    PIWIK_SITE_ID=(str, ""),
    PIWIK_DIMENSION_MAP=(dict, {}),
    GOOGLE_ANALYTICS_ID=(str, ""),
    ALLOWED_HOSTS=(list, []),
    SECRET_KEY=(str, secret_key),
    DB_NAME=(str, os.path.join(BASE_DIR, "db.sqlite3")),
    VALIDATION_ERROR_LOCATIONS_LENGTH=(int, 1000),
    VALIDATION_ERROR_LOCATIONS_SAMPLE=(bool, False),
    DELETE_FILES_AFTER_DAYS=(int, 7),
)

#: Details for Piwik/Matamo tracking, if wanted.
#: Should be a dictionary with the following keys: url, site_id and dimension_map
PIWIK = {
    "url": env("PIWIK_URL"),
    "site_id": env("PIWIK_SITE_ID"),
    "dimension_map": env("PIWIK_DIMENSION_MAP"),
}
#: Details for Google Analytics tracking, if wanted. Should be a string of the id.
GOOGLE_ANALYTICS_ID = env("GOOGLE_ANALYTICS_ID")

VALIDATION_ERROR_LOCATIONS_LENGTH = env("VALIDATION_ERROR_LOCATIONS_LENGTH")
VALIDATION_ERROR_LOCATIONS_SAMPLE = env("VALIDATION_ERROR_LOCATIONS_SAMPLE")

#: Uploaded data is deleted after a certain number of days to protect privacy,
#: leaving only meta data for usage analysis.
#: Should be an integer of the number of days.
DELETE_FILES_AFTER_DAYS = env("DELETE_FILES_AFTER_DAYS")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")


# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "bootstrap3",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "cove.middleware.CoveConfigCurrentApp",
)

ROOT_URLCONF = "cove.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "libcoveweb2.context_processors.from_settings",
            ],
        },
    },
]

WSGI_APPLICATION = ""


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": env("DB_NAME"),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")


LANGUAGES = (
    ("en", "English"),
    ("es", "Spanish"),
)
LOCALE_PATHS = (os.path.join(BASE_DIR, "cove", "locale"),)


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        "": {
            "level": "WARNING",
            "handlers": ["console"],
        },
    },
}

#: Sometimes uploads happen with a generic content type.
#: In this case, we can't rely on content type to detect type.
#: But the type is still allowed. Define these generic content-types in a handy variable
#: so we can also add them to all the ALLOWED_*_CONTENT_TYPES settings.
ALLOWED_UNKNOWN_CONTENT_TYPES = ["application/octet-stream"]

#: Allowed types for JSON files
ALLOWED_JSON_CONTENT_TYPES = ["application/json"] + ALLOWED_UNKNOWN_CONTENT_TYPES
#: Allowed file extensions for JSON files
ALLOWED_JSON_EXTENSIONS = [".json"]

#: Allowed types for Excel files
ALLOWED_SPREADSHEET_EXCEL_CONTENT_TYPES = [
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
] + ALLOWED_UNKNOWN_CONTENT_TYPES
#: Allowed file extensions for Excel files
ALLOWED_SPREADSHEET_EXCEL_EXTENSIONS = [".xlsx"]

#: Allowed types for Open Document files
ALLOWED_SPREADSHEET_OPENDOCUMENT_CONTENT_TYPES = [
    "application/vnd.oasis.opendocument.spreadsheet",
] + ALLOWED_UNKNOWN_CONTENT_TYPES
#: Allowed file extensions for Open Document files
ALLOWED_SPREADSHEET_OPENDOCUMENT_EXTENSIONS = [".ods"]

#: Allowed types for Spreadsheet files (sum of Excel and Open Document)
ALLOWED_SPREADSHEET_CONTENT_TYPES = (
    ALLOWED_SPREADSHEET_EXCEL_CONTENT_TYPES
    + ALLOWED_SPREADSHEET_OPENDOCUMENT_CONTENT_TYPES
)
#: Allowed file extensions for Spreadsheet files (sum of Excel and Open Document)
ALLOWED_SPREADSHEET_EXTENSIONS = (
    ALLOWED_SPREADSHEET_EXCEL_EXTENSIONS + ALLOWED_SPREADSHEET_OPENDOCUMENT_EXTENSIONS
)

#: Allowed types for CSV files
ALLOWED_CSV_CONTENT_TYPES = ["text/csv"] + ALLOWED_UNKNOWN_CONTENT_TYPES
#: Allowed file extensions for CSV files
ALLOWED_CSV_EXTENSIONS = [".csv"]
