
from django.shortcuts import render,HttpResponse, redirect
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.index),
        url(r'^addUser$',views.addUser),
        url(r'find$',views.find)
]
