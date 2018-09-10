"""Demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

from django.contrib import admin
from django.conf.urls import url
from web.views import hello

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'hello/', hello),  # 设置url地址映射
]
"""

from django.conf.urls import *
from django.contrib import admin
from blog.views import *
from django.conf import settings
from django.views.static import serve
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^music/', music),
    url(r'^blogs/$', get_blogs),
    url(r'^detail/(\d+)/$', get_details, name='blog_get_detail'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
