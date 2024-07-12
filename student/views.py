from django.shortcuts import  get_object_or_404
from teacher.models import Course  # Import Course from teacher app
from django.shortcuts import render
from django.db.models import Q  # Import Q objects for OR queries


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
