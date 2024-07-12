from django.urls import path
from . import views
app_name ='student'
urlpatterns = [

    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('explore_course/', views.explore_course, name='explore_course'),
    path('course/<int:course_id>/videos/', views.video_playlist, name='video_playlist'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),

]
