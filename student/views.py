from django.shortcuts import  get_object_or_404
from teacher.models import Course  # Import Course from teacher app
from django.shortcuts import render
from django.db.models import Q  # Import Q objects for OR queries
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from login.forms import StudentProfileForm
from login.models import Student



def student_dashboard(request):
    return render(request, 'student/student_dashboard.html')




def explore_course(request):
    query = request.GET.get('q')
    courses = Course.objects.all()

    if query:
        # Filter by title, description, and teacher's name using OR queries
        courses = courses.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(teacher__first_name__icontains=query) |
            Q(teacher__last_name__icontains=query)
        )

    return render(request, 'student/explore_course.html', {'courses': courses})


def video_playlist(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    videos = course.videos.all()
    return render(request, 'student/video_playlist.html', {'course': course, 'videos': videos})



@login_required
def student_profile(request):
    student = request.user.student
    return render(request, 'student/student_profile.html', {'student': student})

@login_required
def update_profile(request):
    student = request.user.student
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student_profile')
    else:
        form = StudentProfileForm(instance=student)
    return render(request, 'student/update_profile.html', {'form': form})
