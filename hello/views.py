#this imports the ability to do an HttpRequestion which is a special class in django.  in order to use it we must import it
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#in order to create a view in django we must define a function
def index(request):
    return HttpResponse('Hello!')

#create a new view but must associate it with the urls.py
def lyndsey(request):
    return HttpResponse("Hello, Lyndsey") 


#standardize the urls so that it can be anyones name

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")