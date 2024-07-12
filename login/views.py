from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import StudentSignUpForm, TeacherSignUpForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse


def home_view(request):
    return render(request, 'login/home.html')

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login/student_login')  # Redirect to student's login
    else:
        form = StudentSignUpForm()
    return render(request, 'login/student_signup.html', {'form': form})

def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher_login')  # Redirect to teacher's dashboard
    else:
        form = TeacherSignUpForm()
    return render(request, 'login/teacher_signup.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('student:student_dashboard')) # Redirect to student's dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'login/student_login.html', {'form': form})

def teacher_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('teacher:teacher_dashboard'))  # Redirect to teacher's dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'login/teacher_login.html', {'form': form})








def custom_logout(request):
    logout(request)
    return redirect(reverse('login:home'))
