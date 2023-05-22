from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, "myapp/index.html", {})

def register(request):
    return render(request, "myapp/register.html", {})

def login(request):
    return render(request, "myapp/login.html", {})

def home(request):
    return render(request, "myapp/home.html", {})

def aboutus(request):
    return render(request, "myapp/aboutus.html", {})

def contact(request):
    return render(request, "myapp/contact.html", {})
