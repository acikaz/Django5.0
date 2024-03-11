import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ShowDateTimeInfo(request):
    TodaysDate = datetime.datetime.now()
    templatefilename = "djangobasicapp/ShowTimeInfo.html"
    dict={'TodaysDate': TodaysDate}
    return(render(request, templatefilename, dict))
