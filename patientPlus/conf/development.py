# Developement Settings
from .base import *
from decouple import config

SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEV_DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"


STATIC_URL = "static/"

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR, "static"]
else:
    STATIC_ROOT = BASE_DIR / "static"
