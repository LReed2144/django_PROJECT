#this imports the ability to do an HttpRequestion which is a special class in django.  in order to use it we must import it
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#in order to create a view in django we must define a function


#to use an html template instead of writing in all the structure into the function
def index(request):
    return render(request, "hello/index.html")

#create a new view but must associate it with the urls.py
def lyndsey(request):
    return HttpResponse("Hello, Lyndsey") 


#standardize the urls so that it can be anyones name
#this is for the template as well
def greet(request, name):
    return render(request, "hello/greet.html", {
    #this is a dictionary
        "name": name.capitalize()
    })