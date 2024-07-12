from django.urls import path
from . import views

urlpatterns = [
    #path('login/', views.student_login, name='student_login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
path('explore_course/', views.explore_course, name='explore_course'),
path('course/<int:course_id>/videos/', views.video_playlist, name='video_playlist'),

]
