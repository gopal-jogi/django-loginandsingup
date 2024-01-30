from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hell")

def signup(request):
    return render(request,'signup.html') 

def signin(request):
    return render(request,'signin.html') 

def signout(request):
    return render(request,'signout.html') 