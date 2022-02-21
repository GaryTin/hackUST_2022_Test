from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def home(request):
    peoples = People.objects.all()
    if request.method == 'GET': #handle get request
        prform = PeopleRegistrationForm()
        return render(request,'TestApp/home.html',
                      {
                          'peoples' : peoples,
                          'prform': prform,
                      })
    elif request.method =="POST": #handle post request
        prform = PeopleRegistrationForm(request.POST,request.FILES) #create form with Post data
        if prform.is_valid(): #check valid
            prform.save() #save to DB
            return redirect("success")
        else:
            return render(request, 'TestApp/home.html',
                          {
                              'peoples': peoples,
                              'prform': prform,
                          })

def success(request):
    return render(request, 'TestApp/success.html')

def toilet(request):
    return render(request, 'TestApp/toilet.html')

def personal(request,people_slug):
    try:
        peoples = People.objects.get(slug=people_slug)

        return render(request, 'TestApp/personal.html',
                      {
                            'selected_people' : peoples,
                            'people_found': True,
                      })
    except Exception as exc:
        return render(request, 'TestApp/personal.html',
                      {
                          'people_found':False,

                      })