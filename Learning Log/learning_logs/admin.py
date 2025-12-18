from django.contrib import admin

# Register your models here.
# imports the model we want to register, Topic
from .models import Topic, Entry

#tells Django to manage our model through the admin site
admin.site.register(Topic)
admin.site.register(Entry)
