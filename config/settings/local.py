# flake8: noqa

from .base import *

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
