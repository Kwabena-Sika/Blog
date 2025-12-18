from django.contrib import admin
from . models import BlogTopic,BlogEntry
# Register your models here.
admin.site.register(BlogTopic)
admin.site.register(BlogEntry)
