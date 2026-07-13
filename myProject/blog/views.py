from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the blog home page!")

def about(request):
    a = 10+50
    return HttpResponse(f"About page: {a}")

def contact(request):
    a= 5
    b= 6
    c = a+b
    return HttpResponse(f"contact on: {c}")