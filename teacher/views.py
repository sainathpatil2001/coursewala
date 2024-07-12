import datetime
from .models import Course, Video
from .forms import CourseForm, VideoForm
from django.contrib.auth import logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeacherProfileForm
from .models import Teacher
from django.shortcuts import  redirect
from .models import Video

import os
from django.conf import settings

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course
from login.models import Teacher  # Adjust the import path as per your project structure

@login_required
def teacher_dashboard(request):
    try:
        teacher_profile = request.user.teacher_profile
        courses = Course.objects.filter(teacher=teacher_profile)
    except Teacher.DoesNotExist:
        # Handle case where the teacher profile doesn't exist
        courses = []

    return render(request, 'teacher/teacher_dashboard.html', {'courses': courses})


@login_required
def upload_course(request):
    return render(request, 'teacher/upload_course.html')
@login_required
def update_course(request):
    return render(request, 'teacher/update_course.html')
def custom_logout(request):
    logout(request)
    return redirect(reverse('login:teacher_login'))
from django.shortcuts import get_object_or_404

@login_required
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, teacher=request.user.teacher_profile)
    if request.method == 'POST':
        course.delete()
        return redirect('teacher:teacher_dashboard')
    return render(request, 'teacher/delete_course.html', {'course': course})


@login_required
def profile(request):
    # Retrieve the Teacher instance associated with the logged-in user
    teacher = request.user.teacher_profile  # Assuming `teacher_profile` is related name

    context = {
        'teacher': teacher,
    }
    return render(request, 'teacher/profile.html',context)



@login_required
def upload_profile(request):
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES)
        if form.is_valid():
            teacher_profile = form.save(commit=False)
            teacher_profile.user = request.user
            teacher_profile.save()
            return redirect('teacher:profile')  # Adjust the redirect as needed
    else:
        form = TeacherProfileForm()
    return render(request, 'teacher/upload_profile.html', {'form': form})


@login_required
def update_profile(request):
    try:
        teacher_profile = request.user.teacher_profile
    except Teacher.DoesNotExist:
        teacher_profile = None

    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES, instance=teacher_profile)
        if form.is_valid():
            form.save()
            return redirect('teacher:profil')  # Adjust the redirect as needed
    else:
        form = TeacherProfileForm(instance=teacher_profile)

    return render(request, 'teacher/update_profile.html', {'form': form})

#Uplaod cource details view

@login_required
def upload_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)  # Added request.FILES to handle file uploads
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user.teacher_profile
            course.course_number = Course.objects.filter(teacher=course.teacher).count() + 1
            course.save()
            return redirect('teacher:upload_video', course_id=course.id)
    else:
        form = CourseForm()

    # Get the list of uploaded courses for the current teacher
    uploaded_courses = Course.objects.filter(teacher=request.user.teacher_profile)

    return render(request, 'teacher/upload_course.html', {'form': form, 'uploaded_courses': uploaded_courses})


@login_required
def upload_video(request, course_id):
    course = Course.objects.get(id=course_id)
    videos = Video.objects.filter(course=course)  # Get all videos for the course

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.course = course
            video.video_number = Video.objects.filter(course=course).count() + 1
            video.uploaded_at = datetime.datetime.now()  # Set upload timestamp
            video.save()
            return redirect('teacher:upload_video', course_id=course_id)
    else:
        form = VideoForm()

    return render(request, 'teacher/upload_video.html', {'form': form, 'course': course, 'videos': videos})


@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    course_id = video.course.id

    # Get the path of the video file
    video_path = os.path.join(settings.MEDIA_ROOT, str(video.video_file))

    # Check if the file exists before deletion
    if os.path.exists(video_path):
        os.remove(video_path)  # Delete the file from the filesystem

    # Delete the video object from the database
    video.delete()

    return redirect('teacher:upload_video', course_id=course_id)
