from django.contrib import admin

from .models import Bio, Language, Tool, Job, Contact

admin.site.register(Bio)
admin.site.register(Language)
admin.site.register(Tool)
admin.site.register(Job)
admin.site.register(Contact)