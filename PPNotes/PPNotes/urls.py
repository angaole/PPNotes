"""PPNotes URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from new_app import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
    url(r'^browse/(.+)/(.+)/$', views.browse),
    url(r'^searchby/(.+)/', views.searchby),
    url(r'^search/', views.search),
    url(r'^download/', views.download),
    url(r'^help/', views.help),
    url(r'^result/(.+)/', views.result),
    url(r'^data/(.+)/', views.data),
    url(r'^test/', views.test),
    url(r'^searchfor/(.+)/$', views.searchfor),
    url(r'^savegene/(.+)/', views.savegene),
    url(r'^savedise/(.+)/', views.savedise),
    url(r'^saveexpre/(.+)/', views.saveexpre),
    url(r'^showpic/(.+)/(.+)/$', views.showpic),
]
