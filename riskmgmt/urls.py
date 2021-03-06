"""riskmgmt URL Configuration

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
from main_module.views_pkg import (IndexView)
from main_module.views_pkg.func_view import (register,)
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_module/', include('main_module.urls')),
    path('', IndexView.IndexView.as_view(), name='index'),
    path('welcome', IndexView.IndexView.as_view(), name='welcomepage'),
    url(r'^register/$',register.register,name="register"),
    url(r'^signup/$',register.register,name="signup"),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name="registeration/logout.html"),
        name="logout"),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="registeration/login.html",
                                                 redirect_field_name="main_module/home"),
        name="login"),
]
