from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.fields.related import OneToOneField

class User(AbstractUser):
  is_student = models.BooleanField(default=False)
  is_teacher = models.BooleanField(default=False)
  course = models.CharField(max_length=100)


class Student(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  phone_number = models.CharField(max_length=20)
  comment = models.CharField(max_length=100)


class Teacher(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  phone_number = models.CharField(max_length=20)
  hostel = models.CharField(max_length=100)

