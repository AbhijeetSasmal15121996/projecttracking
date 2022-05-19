from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import Category

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hodsignin(request):
    return render(request, 'signin.html', {'data': 'hod'})

def hodsignup(request):
    return render(request, 'signup.html', {'data': 'hod'})

def corsignup(request):
    return render(request, 'signup.html', {'data': 'coor'})

def corsignin(request):
    return render(request, 'signin.html', {'data': 'coor'})

def guidesignin(request):
    return render(request, 'signin.html', {'data': 'guide'})

def guidesignup(request):
    return render(request, 'signup.html', {'data': 'guide'})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        type = request.POST['type']
        user = User.objects.create_user(username, username+'@email.com', password)
        cat = Category(user=user, category=type)
        return redirect(type+'signup')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        type = request.POST['type']
        u = authenticate(username=username, password=password)
        cat = Category.objects.filter(user=u)
        if len(cat)==0:
            login(request, u)
            return redirect(type+'signin')