from django.db import models
from django.contrib import admin
from django.contrib.gis.db.models.functions import Length
from sqlite3.dbapi2 import Timestamp

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    Timestamp = models.DateTimeField()
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(Blog, BlogAdmin)
