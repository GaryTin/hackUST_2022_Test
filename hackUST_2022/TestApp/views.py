from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    peoples = People.objects.all()
    return render(request,'TestApp/home.html',
                  {
                      'peoples' : peoples,
                  })

def toilet(request):
    return render(request, 'TestApp/toilet.html')

def personal(request,people_slug):
    peoples = People.objects.get(slug=people_slug)
    return render(request, 'TestApp/personal.html',
                  {
                      'selected_people' : peoples,

                  })