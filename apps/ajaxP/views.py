from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from datetime import datetime
from django.core import serializers
import json
# Create your views here.
def index(request):
    return render(request,'ajaxP/index.html')


def addUser(requset):
    print(requset.POST['name'])
    return redirect('/')

def find(request):
    
    
    toDate=request.POST["date"]
    fromDate=request.POST["from"]
    print ("here's the date after casting form ",toDate)
    if toDate=="":
        usrs =Users.objects.filter(first_name__startswith=request.POST["name"])
        print ("to date is null")
    else:
        print ('date is not empty')
        usrs =Users.objects.filter(first_name__startswith=request.POST["name"]).filter(registered_datetime__range=(fromDate,toDate))
       
    return render(request,'ajaxP/table.html',{"users":usrs})
    
    

    
    
    