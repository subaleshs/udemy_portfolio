from portfolio.settings import TIME_ZONE
from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import course


def home(request):

    """
    Get to the home page

    request: HttpRequest object

    Returns home page with list of courses
    
    """
    print(datetime.now())
    courseCat = course.objects.all()
    print(courseCat)
    return render(request,'portfapp\ind.html',{'courses':courseCat})



def details(request,crid):

    """
    Get details about a course

    request: HttpRequest object

    crid: primary key of the course

    Returns the details of a particular course
    
    """

    val = course.objects.get(pk=crid)
    return render(request,'portfapp/details.html',{'course':val})
