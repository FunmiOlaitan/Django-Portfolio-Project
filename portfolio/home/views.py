from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    return render(request, 'home.html')

def projects(request):
    #return HttpResponse("This is my homepage (/projects)")
    return render(request, 'projects.html')

def highlights(request):
    #return HttpResponse("This is my homepage (/highlights)")
    return render(request, 'highlights.html')

def contact(request):
    if request.method=="POST":
        print("This is post ")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the db")

    #return HttpResponse("This is my homepage (/contacts)")
    return render(request, 'contact.html')
