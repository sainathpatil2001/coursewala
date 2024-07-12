# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    email = models.EmailField(unique=True)  # Add email field

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional student fields here, e.g., grade, major, etc.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional teacher fields here, e.g., department, courses, etc.
