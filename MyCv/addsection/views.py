from django.shortcuts import render
from .models import JobTitle, Summary
from django.http import HttpResponse

# Create your views here.
def index(request):

    lastest_cv_introduced = applicant_cv(1)
    return HttpResponse("hello world")

def job_name(request, job_id):
    response = "You are looking at the results for %s"
    return HttpResponse(response % job_id)

def submit_data(request):
    return HttpResponse("Please enter you CV data")
