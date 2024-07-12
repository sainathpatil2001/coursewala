# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
# models.py
from django.conf import settings
from django.db import models

from django.utils import timezone

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    email = models.EmailField(unique=True)  # Add email field

from django.contrib.auth.models import User
from django.db import models



def student_image_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/student_profile_image/<student_id>/filename
    return f'student_profile_image/{instance.user.id}/{filename}'

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10, blank=True, null=True)
    major = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to=student_image_path, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    enrolled_courses = models.ManyToManyField('Course', through='Enrollment')
    completed_courses = models.ManyToManyField('Course', related_name='completed_courses', blank=True)
    wishlist = models.ManyToManyField('Course', related_name='wishlist', blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instructor')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DurationField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Progress percentage
    last_accessed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.user.username} enrolled in {self.course.title}"
