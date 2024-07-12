from .models import Teacher
from django import forms
from .models import Course, Video

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'address', 'biography',
            'profile_picture', 'date_of_birth', 'education', 'experience'
        ]




class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'course_image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'video_file')