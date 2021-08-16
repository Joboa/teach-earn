from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login
from .models import User
from .forms import StudentSignUpForm, TeacherSignUpForm

# Create your views here.
# def home(request):
#   return render(request, template_name="base.html")

class HomeView(TemplateView):
  template_name = 'home.html'


def register(request):
  return render(request, template_name="register/register.html")

class student_register(CreateView):
  model = User
  form_class = StudentSignUpForm
  template_name = 'register/student_register.html'

class teacher_register(CreateView):
  model = User
  form_class = TeacherSignUpForm
  template_name = 'register/teacher_register.html'

# class SignupPageView(generic.CreateView):
#   form_class = CustomUserCreationForm
#   success_url = reverse_lazy('login')
#   template_name = 'signup.html'