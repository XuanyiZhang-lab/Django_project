from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Photo, BlogPost

admin.site.register(Photo)
admin.site.register(BlogPost)
