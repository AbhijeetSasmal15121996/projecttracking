from statistics import mode
from django.contrib.auth.models import User
from django.db import models
import uuid


# Create your models here.
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)


class Panel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    panel_name = models.CharField(max_length=200)


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    panel_id = models.ForeignKey(Panel, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    flag = models.BooleanField(default=False)


class Guide(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    panel_id = models.ForeignKey(Panel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Team(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, null=True)
    team = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Student(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    batch = models.CharField(max_length=200)
    roll_no = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email_id = models.CharField(max_length=200)

class Review(models.Model):
    review_name = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
    date = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    venue= models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)