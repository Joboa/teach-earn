from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from allauth.account.views import SignupView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from .models import User
from .forms import StudentSignUpForm, TeacherSignUpForm, LoginForm

"""
Home page
"""
class HomeView(TemplateView):
    template_name = 'home.html'

"""
Register a person (student or teacher)
"""
def register(request):
    return render(request, template_name="register/register.html")


"""
Student registration form
"""
class student_register(SignupView):
    model = User
    form_class = StudentSignUpForm
    success_url = reverse_lazy('verify_account')
    # redirect_field_name = 'next'
    # success_url = None
    template_name = 'register/student_register.html'

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        ret['user_type'] = "is_student"
        return ret


"""
Teacher registration form
"""
class teacher_register(SignupView):
    model = User
    form_class = TeacherSignUpForm
    success_url = reverse_lazy('verify_account')
    template_name = 'register/teacher_register.html'

    def get_context_data(self, **kwargs):
        ret = super().get_context_data(**kwargs)
        ret['user_type'] = "is_teacher"
        return ret

class verification_sent(TemplateView):
    template_name = 'account/verification_sent.html'

"""
Login forms to direct a user based on type (student or teacher) 
choosen during registraion
"""
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
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

"""
Student profile page
"""
class StudentProfileView(TemplateView):
    template_name = 'student_page.html'


"""
Teacher profile page
"""
class TeacherProfileView(TemplateView):
    template_name = 'teacher_page.html'
