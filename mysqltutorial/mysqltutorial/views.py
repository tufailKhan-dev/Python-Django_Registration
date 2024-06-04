from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from mysqltutorial.models import mysqldata
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data = mysqldata.objects.all()
    mydata = {
        'data':data
    }
    return render(request,"index.html",mydata)

