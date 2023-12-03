from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from mysqltutorial.models import mysqldata
from django.contrib.auth import logout
from django.contrib import messages
def index(request):
    data = mysqldata.objects.all()
    mydata = {
        'data':data
    }
    return render(request,"index.html",mydata)

