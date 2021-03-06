"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
"""
from argparse import Namespace
from unicodedata import name
from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from xmlrpc.client import Server
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls'), name='project'),
    path('downloadfile',include('downloadapp.urls'),name='dwonlode'),
    # url(r'^media/(?P<path>.*)$', Server,{'document_root': settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', Server,{'document_root': settings.STATIC_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
