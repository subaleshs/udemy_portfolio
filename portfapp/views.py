from portfolio.settings import TIME_ZONE
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import course


def home(request):
    print(datetime.now())
    courseCat = course.objects.all()
    print(courseCat)
    return render(request,'portfapp\ind.html',{'courses':courseCat})

def details(request,crid):
    val = course.objects.get(pk=crid)
    # print(v)
    # val = get_list_or_404(course,pk=crid)
    # print(val)
    return render(request,'portfapp/details.html',{'course':val})
