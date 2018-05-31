from django.db import models
from django.contrib import admin
from cryptography.hazmat.primitives.ciphers import modes


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

admin.site.register(Blog, BlogAdmin)

#在这里创造你自己的模板
#作者
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def _unicode_(self):
        return self.first_name
    

#出版商
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province =models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def _unicode_(self):
        return self.name
    
#书
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,)
    publication_date = models.DateField()
    
    def _unicode_(self):
        return self.title