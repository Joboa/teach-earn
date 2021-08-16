from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .models import User
from .forms import StudentSignUpForm, TeacherSignUpForm, LoginForm


class HomeView(TemplateView):
  template_name = 'home.html'


def register(request):
  return render(request, template_name="register/register.html")

class student_register(CreateView):
  model = User
  form_class = StudentSignUpForm
  success_url = reverse_lazy('register/login/')
  template_name = 'register/student_register.html'

class teacher_register(CreateView):
  model = User
  form_class = TeacherSignUpForm
  success_url = reverse_lazy('register/login/')
  template_name = 'register/teacher_register.html'


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_student:
                login(request, user)
                return redirect('student_page')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher_page')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

class StudentProfileView(TemplateView):
  template_name = 'student_page.html'

class TeacherProfileView(TemplateView):
  template_name = 'teacher_page.html'