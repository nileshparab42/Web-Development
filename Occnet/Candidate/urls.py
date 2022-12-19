"""Occnet URL Configuration

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
from django.contrib import admin
from django.urls import path
from Candidate import views

urlpatterns = [
    path("", views.index, name="home"),
    path("job/", views.job, name="home"),
    path("about-us/", views.aboutus, name="home"),
    path("jobinfo/", views.infojob, name="info"),
    path("contact-us", views.contactus, name="contactus"),
    path("log-in", views.loginpage, name="login"),
    path("log-out", views.logoutpage, name="login"),
    path("sign-up", views.signuppage, name="signup"),
    path("jobinfo/apply", views.apply, name="apply")
]
