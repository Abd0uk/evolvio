from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse('home page')

def dashboard(request):
    return HttpResponse('Dashboard page')