"""hfe_unist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from hfe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('en/home/about', views.en_about, name="en_about"),
    path('en/home/research', views.en_research, name="en_research"),
    path('en/home/curriculum', views.en_curriculum, name="en_curriculum"),
    path('en/home/faculty', views.en_faculty, name="en_faculty"),
    path('en/', views.en_main, name="en_main"),

    path('ko/home/about', views.ko_about, name="ko_about"),
    path('ko/home/research', views.ko_research, name="ko_research"),
    path('ko/home/curriculum', views.ko_curriculum, name="ko_curriculum"),
    path('ko/home/faculty', views.ko_faculty, name="ko_faculty"),
    path('ko/', views.ko_main, name="ko_main"),
]
