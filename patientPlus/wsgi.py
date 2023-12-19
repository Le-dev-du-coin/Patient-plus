import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patientPlus.conf.prod")

application = get_wsgi_application()
