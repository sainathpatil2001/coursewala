from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='teacher'
urlpatterns = [
    # path('login/', views.student_login, name='student_login'),
    #path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('upload_course/', views.upload_course, name='upload_course'),
    path('update_course', views.update_course, name='update_course'),
    path('upload_video/<int:course_id>/', views.upload_video, name='upload_video'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('delete_course', views.delete_course, name='delete_course'),
    path('profil/', views.profile, name='profil'),
    path('logout/', views.custom_logout, name='logout'),
    path('upload_profile/', views.upload_profile, name='upload_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),

    path('upload_course/', views.upload_course, name='upload_course'),
    path('upload_video/<int:course_id>/', views.upload_video, name='upload_video'),
    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('delete_course/<int:course_id>/', views.delete_course, name='delete_course'),
]


