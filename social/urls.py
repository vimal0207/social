"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from signup import views as sview
from login import views as lview
from userprofile import views as uview
from urllib.parse import unquote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lview.loginview,  name='login'),
    path('login/', lview.loginview,  name='login'),
    path('logout/', lview.logout,  name='logout'),
    path('signup/', sview.signupview, name='signup'),
    path('validate/', sview.validateview,  name='validate'),
    path('home/', uview.homeview,  name='home'),
    path('search/', uview.searchview,  name='search'),
    path('post/', uview.savepost,  name='post'),
    path('sendrequest/', uview.sendrequest,  name='sendrequest'),
    path('friendprofile/<id>/', uview.friendprofile,  name='friendprofile'),

    
]