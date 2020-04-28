"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
# from django.conf.urls import url
from stud import views
from stud.views import dashboard, home, login, register, updateRegister, deleteRegister, viewall,departmet, studApiView
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('login/', login, name = 'login'),
    path('register/', register, name = 'register'),
    path('updateRegister/<str:pid>/', updateRegister, name = 'updateRegister'),
    path('deleteRegister/<str:pid>/', deleteRegister, name = 'deleteRegister'),
    path('viewall/<str:pid>/', viewall, name = 'viewall'),
    path('dashboard/', dashboard, name = ' dashboard'),
    path('departmet/', departmet, name = 'departmet'),
    # path('studapi/', views.studApiView),
    path('studapi/',studApiView.as_view(), name = 'studapi'),
    # path('api-auth/', include('rest_framework.urls'))
    # path('departmet1/', departmet1, name = 'departmet1'),
]
urlpatterns = format_suffix_patterns(urlpatterns)