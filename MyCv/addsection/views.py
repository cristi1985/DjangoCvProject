from django.shortcuts import render
from .models import Addsection
from django.http import HttpResponse

# Create your views here.
def index(request):

    lastest_cv_introduced = applicant_cv(1)
    return HttpResponse("hello world")

def applicant_cv(request, applicant_id):
    response = "You are looking at the results for %s"
    return HttpResponse(response % applicant_id)

def submit_data(request):
    return HttpResponse("Please enter you CV data")
