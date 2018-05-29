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
  #    response.set_cookie('username',username,3600) #用户名 cookie
      request.session['username']=username #将session信息写到服务器
      return response
    else:
      return render_to_response('index.html', {'error':'username or password error!','blogs':blog_list})
    
    #登录成功
def login_ok(request):
    blog_list=Blog.objects.all()
 #   username = request.COOKIES.get('username','') # read web Cookie
    username = request.session.get('username','')
    return render_to_response('login_ok.html',{'user':username,'blog_list':blog_list})

def loginout(request):
    response = HttpResponseRedirect('/index/') # 返回首页
  #  response.delete_cookie('username') #清理cookie里保存username
    del request.session['username']  #清理用户session
    return response