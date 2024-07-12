from django.db import models
import os
from django.conf import settings
from .utils import course_image_upload_path  # Adjust the import path as per your project structure

import datetime

def teacher_profile_picture_upload_to(instance, filename):
    return os.path.join('profile_pictures', str(instance.user.id), filename)

def course_upload_to(instance, filename):
    return os.path.join('courses', str(instance.teacher.user.id), str(instance.id), filename)

def video_upload_to(instance, filename):
    return os.path.join('courses', str(instance.course.teacher.user.id), str(instance.course.id), 'videos', filename)

class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to=teacher_profile_picture_upload_to, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    course_image = models.ImageField(upload_to=course_image_upload_path, blank=True, null=True)
    course_number = models.IntegerField(default=1)

    def __str__(self):
        return self.title



class Video(models.Model):
    course = models.ForeignKey(Course, related_name='videos', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to=video_upload_to)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_number = models.IntegerField(default=1)


    def __str__(self):
        return self.title