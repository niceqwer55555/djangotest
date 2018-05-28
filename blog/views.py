from django.shortcuts import render_to_response
from blog.models import Blog

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})
