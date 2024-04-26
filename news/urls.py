"""
URL configuration for news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
# from django.conf import settings
# from django.conf.urls.static import static
from xabar.views import all_newss
from xabar.views import  news_create, detail, edit, all_newss, register

from django.conf import settings
from django.conf.urls.static import static


# def index(a):
#     return render(a,"blog-details.html", {'b': ['car', 'book', 'plane']})

def main(a):
  return render(a,"blog.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('uz/', index,name='uz'),
    path('ma/',main,name='ma'),
    path('home/',all_newss,name='uy'),
    path('create/',news_create,name='create'),
    path('detail/<int:a>/', detail, name='detail'),
    path('tahrir/<int:id>/', edit, name = 'edit'),
    path('signup/', register, name='register'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

