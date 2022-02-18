from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'TestApp/home.html')

def toilet(request):
    return render(request, 'TestApp/toilet.html')