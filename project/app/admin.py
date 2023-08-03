from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(event_details)
admin.site.register(event_template)
