from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def top_sellers(request):
    return render(request, "top-sellers.html")

#def login(request):
 #   return render(request, "login.html")
    
#def advertisment(request):
 #   return render(request, "advertisment.html")
    

def advertisment_post(request):
    return render(request, "advertisment-post.html")

#def profile(request):
 #   return render(request, "profile.html")

def register(request):
    return render(request, "register.html")