from django.contrib import admin
from .models.services import Service
from .models.story import Story
from .models.storyupdate import StoryUpdate

admin.site.register(Service)
admin.site.register(Story)
admin.site.register(StoryUpdate)

# Register your models here.
