from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("This is my homepage (/about)")
    return render(request, 'about.html')

def projects(request):
    #return HttpResponse("This is my homepage (/project)")
    return render(request, 'projects.html')

def contact(request):
    #return HttpResponse("This is my homepage (/contacts)")
    return render(request, 'contact.html')
