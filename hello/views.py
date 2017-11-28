# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import Http404
from  hello import models
from datetime import datetime
# Create your views here.

user_list = [
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"ABC"},
]

def index(request):
    #request.POST
    #request.GETs
    #return HttpResponse("hello world!")
    if request.method == "POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #temp = {"user":username,"pwd":password}
        #user_list.append(temp)
        #添加数据到数据库
        models.UserInfo.objects.create(user=username,pwd=password)
    #从数据库读取数据
    user_list = models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})

def Test(request):
    #return HttpResponse("just a test")
    return render(request,'commodity/test.html',{'current_time':datetime.now()})

def home(request):
    post_list = models.Article.objects.all();
    return render(request,'commodity/home.html',{'post_list':post_list})

def Detail(request,id):
    try:
        post = models.Article.objects.get(id=str(id))
    except models.Article.DoesNotExist:
        raise Http404
    return render(request,'commodity/post.html',{'post':post})
