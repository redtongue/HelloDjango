"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from hello import views
import hello.urls as blog_url
from DjangoUeditor import urls as djud_urls
from django.conf import settings

urlpatterns = [
    #url(r'^',views.Test),
    url(r'^admin/', admin.site.urls),
    url(r'^index/',views.index),
    url(r'^test/',views.Test),
    url(r'^ueditor/',include(djud_urls)),
    url(r'^home/',views.home,name="blog_home"),
    url(r'^post/(?P<id>\d+)/$',views.Detail,name="blog_detail"),
    url(r'^category/(?P<category>\w+)/$',views.list_category,name="blog_category"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
