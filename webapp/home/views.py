from datetime import date
from time import time
from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hodsignin(request):
    return render(request, 'signin.html', {'data': 'hod'})

def hodsignup(request):
    return render(request, 'signup.html', {'data': 'hod'})

def corsignup(request):
    return render(request, 'signup.html', {'data': 'cord'})

def corsignin(request):
    return render(request, 'signin.html', {'data': 'cord'})

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
        cat.save()
        return redirect(type+'signup')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        type = request.POST['type']
        u = authenticate(username=username, password=password)
        cat = Category.objects.filter(user=u)
        if len(cat):
            login(request, u)
            return redirect(type)
        else:
            return redirect('hodsignin')

# Cordinator Job Create panel create and add project add guide to panel
def cordination(request):
    p1 = Panel.objects.all()
    g1 = Category.objects.filter(category='guide')
    g2 = Guide.objects.all()
    t1 = Team.objects.all()
    if request.method == 'POST':
        if 'panel' in request.POST:
            panel = request.POST['panel']
            p = Panel(panel_name=panel)
            p.save()
        if 'project' in request.POST:
            project = request.POST['project']
            panel_id = request.POST['panel_id']
            pr = Project(panel_id=panel_id, project_name=project )
            pr.save()
        if 'guide' in request.POST:
            user = request.POST['guide']
            u = User.objects.filter(username=user)[0]
            panel_id = request.POST['panel_id']
            p = Panel.objects.filter(id=panel_id)[0]
            g = Guide(panel_id=p, user=u)
            g.save()
        if 'team' in request.POST:
            guide = request.POST['guide']
            g = Guide.objects.filter(id=guide)[0]
            user = request.POST['user']
            u = User.objects.filter(id=user)[0]
            t = Team(team=user, guide=g)
            t.save()
    return render(request, 'cord.html', {'panels':p1, 'guides': g1, 'guide': g2, 'team': t1})

    def cord_details(request):
        panels = Panel.objects.all()
        projects = Project.objects.all()
        guide = Guide.objects.all()
        team = Team.objects.all()
        return render(request, 'cord_details.html', {'panel': panels, 'project':projects, 'guide':guide, 'team':team})

    def coorreview(request):
        review = Review.objects.all()
        if request.method == 'POST':
            review_name = request.POST['review_name']
            team = request.POST['id']
            date = request.POST['date']
            time = request.POST['time']
            venue = request.POST['venue']
            t = Team.objects.filter(id=team)[0]
            r = Review.objects.filter(team=t, review_name=review_name)
            if len(r) == 0:
                s = Student.objects.filter(team=t)
                for x in s:
                    r = Review(review_name=review_name, student=s, date=date,time=time, venue=venue, team=t)
                    r.save()
            else:
                for x in r:
                    if date != "":
                        x.date = date
                    if time != "":
                        x.time = time
                    if venue != "":
                        x.venue = venue
                    x.save()
            return render(request, 'corview.html', {'data': review})
        return render(request, 'corview.html', {'data': review})

