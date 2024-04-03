from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my homepage (/)")
def about(request):
    return HttpResponse("This is my homepage (/about)")
def projects(request):
    return HttpResponse("This is my homepage (/project)")
def contact(request):
    return HttpResponse("This is my homepage (/contacts)")
