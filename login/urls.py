from django.urls import path,include
from . import views
app_name='login'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('student_login/', views.student_login, name='student_login'),
    path('teacher_login/', views.teacher_login, name='teacher_login'),
    path('student_signup/', views.student_signup, name='student_signup'),
    path('teacher_signup/', views.teacher_signup, name='teacher_signup'),
    #path('student_dashboard/', views.student_dashboard, name='student_dashboard'),  # Add your student dashboard view
    #path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),  # Add your teacher dashboard view
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
    path('logout/', views.custom_logout, name='logout'),
]
