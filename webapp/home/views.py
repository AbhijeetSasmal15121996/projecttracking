from datetime import date
from time import time
from unicodedata import category
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as lgt

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
        if type == 'team':
            return redirect('teamsignup1')
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
            p = Panel.objects.filter(id=panel_id)[0]
            pr = Project(panel_id=p, project_name=project )
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

def logout(request):
    lgt(request)
    return redirect('home')

def hod(request):
    return redirect('corview')

def teamsignup1(request):
    user = request.user
    pro = Project.objects.filter(flag=False)
    if request.method == 'POST':
        project_id = request.POST['project_id']
        batch = request.POST['batch']
        
        roll1 = request.POST['roll1']
        phone1 = request.POST['phone1']
        email1 = request.POST['email1']

        roll2 = request.POST['roll2']
        phone2 = request.POST['phone2']
        email2 = request.POST['email2']
        
        roll3 = request.POST['roll3']
        phone3 = request.POST['phone3']
        email3 = request.POST['email3']
        
        roll4 = request.POST['roll4']
        phone4 = request.POST['phone4']
        email4 = request.POST['email4']

        p = Project.objects.filter(id=project_id)[0]
        t = Team(team=user, project=p)
        t.save()
        s1 = Student(team=t, batch=batch, roll_no=roll1, phone=phone1, email=email1)
        s1.save()
        s2 = Student(team=t, batch=batch, roll_no=roll2, phone=phone2, email=email2)
        s2.save()
        s3 = Student(team=t, batch=batch, roll_no=roll3, phone=phone3, email=email3)
        s3.save()
        s4 = Student(team=t, batch=batch, roll_no=roll4, phone=phone4, email=email4)
        s4.save()
        p.flag = True
        p.save()
        return redirect('logout')
    return render(request, 'teamsignup1.html', {'project': pro})

def guide(request):
    t = Team.objects.all()
    if request.method == 'POST':
        t1 = request.POST['id']
        t1 = Team.objects.filter(id=t1)[0]
        st = Student.objects.filter(team=t)
        return render(request, 'guide.html', {'data':st, 'team': t})
    return render(request, 'guide.html', {'team': t})

def guides(request):
    if request.method == 'POST':
        st = request.POST['id']
        s = Student.objects.filter(id=id)[0]
        marks = request.POST['marks']
        s.marks = marks
        s.save()
        return redirect('guide')

def team(request):
    team = request.user
    t = Team.objects.filter(team=t)[0]
    st = Student.objects.filter(team=t)
    r = Review.objects.filter(team=t)
    return render(request, 'team.html', {'s':st, 're':r})

