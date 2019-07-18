from django.contrib import admin
from .models.services import Service
from .models.story import Story

admin.site.register(Service)
admin.site.register(Story)

# Register your models here.
