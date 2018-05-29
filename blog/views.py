from django.shortcuts import render_to_response
from blog.models import Blog
from django.http import HttpResponse

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})

def login(request):
    blog_list = Blog.objects.all()
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    if username == 'laji' and password == 'laji':
        return HttpResponse('login success!')
    else:
        return render_to_response('index.html', {'error':'username or password error!','blogs':blog_list})