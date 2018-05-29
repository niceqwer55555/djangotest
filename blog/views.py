from django.shortcuts import render_to_response
from blog.models import Blog
from django.http import HttpResponse
from requests.models import Response
from django.http.response import HttpResponseRedirect
from http.cookiejar import Cookie
from softwareproperties.cloudarchive import WEB_LINK

# Create your views here.
def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})

def login(request):
    blog_list = Blog.objects.all()
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    if username != '' and password != '':
      #  return HttpResponse('login success!')
      response = HttpResponseRedirect('/login_ok/')
      response.set_cookie('username',username,3600) #user cookie
      return response
    else:
      return render_to_response('index.html', {'error':'username or password error!','blogs':blog_list})
    
    #login success
def login_ok(request):
    blog_list=Blog.objects.all()
    username = request.COOKIES.get('username','') # read web Cookie
    return render_to_response('login_ok.html',{'user':username,'blog_list':blog_list})

def loginout(request):
    response = HttpResponseRedirect('/index/') # 返回首页
    response.delete_cookie('username') #清理cookie里保存username
    return response