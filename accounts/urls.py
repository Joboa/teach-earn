from django.urls import path
from .views import HomeView, register, student_register, teacher_register

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('register/', register, name='register'),
  # path('signup/', SignupPageView.as_view(), name='signup'),
  path('student_register/', student_register.as_view(), name='student_register'),
  path('teacher_register/', teacher_register.as_view(), name='teacher_register'),

]