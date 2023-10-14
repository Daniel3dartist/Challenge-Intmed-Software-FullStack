from django.contrib import admin
from .models import Doctor, Schedule

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Schedule)