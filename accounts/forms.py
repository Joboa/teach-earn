# from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django.db import transaction
from .models import User, Student, Teacher
from django import forms


class StudentSignUpForm(SignupForm):
    
    class Meta:
        model = User

    @transaction.atomic
    def save(self, request):
        user = super(StudentSignUpForm, self).save(request)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user


class TeacherSignUpForm(SignupForm):
 
    class Meta:
        model = User

    @transaction.atomic
    def save(self, request):
        user = super(TeacherSignUpForm, self).save(request)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        teacher.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password',)
