# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Teacher

class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Save the email from the form
        user.is_student = True
        if commit:
            user.save()
            Student.objects.create(user=user)
        return user

class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
            Teacher.objects.create(user=user)
        return user

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['grade', 'major', 'profile_picture', 'bio', 'date_of_birth', 'address', 'phone_number']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
