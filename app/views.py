from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
import uuid


def login_view(request):
    if request.POST:
        userName = request.POST.get('username')
        pWord = request.POST.get('password')
        
        user = authenticate(request, username=userName, password=pWord)
        
        if user is not None:
            login(request, user)
            token = str(uuid.uuid4())  
            request.session['token'] = token 
            return redirect('dashboard')
        else:
            return redirect('login')
        
    return render(request , "login.html" )    


def logout_view(request):
  try:
    del request.session['token']
    logout(request)
    return redirect("login")
  
  except KeyError:
    pass


@login_required(login_url="login")
def dashboard(request):
    return render(request , "dashboard.html")