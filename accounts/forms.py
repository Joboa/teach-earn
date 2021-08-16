from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Student, Teacher
from django import forms

class StudentSignUpForm(UserCreationForm):
  course = forms.CharField(required=True)
  phone_number = forms.CharField(required=True)
  comment = forms.CharField(required=True)

  class Meta(UserCreationForm.Meta):
    model = User
    fields = ('username','email',)

  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_student = True
    user.course = self.cleaned_data.get('course')
    user.save()
    student = Student.objects.create(user=user)
    student.phone_number = self.cleaned_data.get('phone_number')
    student.comment = self.cleaned_data.get('comment') 
    student.save()
    return student


class TeacherSignUpForm(UserCreationForm):
  course = forms.CharField(required=True) 
  phone_number = forms.CharField(required=True)
  hostel = forms.CharField(required=True)

  class Meta(UserCreationForm.Meta):
    model = User

  @transaction.atomic
  def save(self):
    user = super().save(commit=False)
    user.is_teacher = True
    user.course = self.cleaned_data.get('course')
    user.save()
    teacher = Teacher.objects.create(user=user)
    teacher.phone_number = self.cleaned_data.get('phone_number')
    teacher.hostel = self.cleaned_data.get('hostel')
    teacher.save()
    return teacher

  