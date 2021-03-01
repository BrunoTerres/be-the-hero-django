from django.contrib import admin

from .models import Ngo, Incidents

admin.site.register(Ngo)
admin.site.register(Incidents)