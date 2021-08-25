from accounts.views import student_register
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import User, Student, Teacher
from .views import student_register, teacher_register

"""
Test for creating a new user
"""
class CustomUserTests(TestCase):

  def test_create_user(self):
    user = User.objects.create_user(
      username="john",
      email="john@joboadevs.com",
      password="joboa"
    )

    self.assertEqual(user.username, "john")
    self.assertEqual(user.email, "john@joboadevs.com")
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_student)
    self.assertFalse(user.is_teacher)
    self.assertFalse(user.is_staff)
    self.assertFalse(user.is_superuser)

  
  def test_create_superuser(self):
      admin_user = User.objects.create_superuser(
      username="admin",
      email="admin@joboadevs.com",
      password="joboa"
    )

      self.assertEqual(admin_user.username, "admin")
      self.assertEqual(admin_user.email, "admin@joboadevs.com")
      self.assertTrue(admin_user.is_active)
      self.assertFalse(admin_user.is_student)
      self.assertFalse(admin_user.is_teacher)
      self.assertTrue(admin_user.is_staff)
      self.assertTrue(admin_user.is_superuser)


"""
Test student model
"""
class StudentUserTests(TestCase):
  def test_create_student_user(self):
    user = User.objects.create_user(
      username="john",
      email="john@joboadevs.com",
      password="joboa"
    )
    student_user = Student(
      user=user,
      phone_number="123444444",
      comment="great"
    )

    self.assertEqual(student_user.user.username, user.username)
    self.assertEqual(student_user.user.email, user.email)
    self.assertEqual(student_user.phone_number, "123444444")
    self.assertEqual(student_user.comment, 'great')


"""
Test teacher model
"""
class TeacherUserTests(TestCase):
  def test_create_teacher_user(self):
    user = User.objects.create_user(
      username="teacher",
      email="teacher@joboadevs.com",
      password="joboa"
    )
    teacher_user = Teacher(
      user=user,
      phone_number="123444444",
      hostel="evandy"
    )

    self.assertEqual(teacher_user.user.username, user.username)
    self.assertEqual(teacher_user.user.email, user.email)
    self.assertEqual(teacher_user.phone_number, "123444444")
    self.assertEqual(teacher_user.hostel, 'evandy')


"""
Test student signup form
"""
class StudentSignupTests(TestCase):

  username = "studentuser"
  email = "studentuser@joboadevs.com"

  def setUp(self):
    url = reverse('student_register')
    self.response = self.client.get(url)
    self.view = resolve('/accounts/student_register/')

  def test_student_signup_template(self):
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'register/student_register.html')
    self.assertContains(self.response, "Student")
    self.assertNotContains(self.response, 'Teachers')
    self.assertEqual(
      self.view.func.__name__, student_register.as_view().__name__
    )

  def test_student_signup_form(self):
    student_user = User.objects.create_user(
      self.username, self.email, is_student=True, is_teacher=False
    )
    self.assertEqual(User.objects.all().count(), 1)
    self.assertEqual(User.objects.all()[0].username, self.username)
    self.assertEqual(User.objects.all()[0].email, self.email)
    self.assertTrue(student_user.is_student, True)
    self.assertFalse(student_user.is_teacher, False)



"""
Test teacher signup form
"""
class TeacherSignupTests(TestCase):
  
  username = "teacheruser"
  email = "teacheruser@joboadevs.com"

  def setUp(self):
    url = reverse('teacher_register')
    self.response = self.client.get(url)
    self.view = resolve('/accounts/teacher_register/')

  def test_teacher_signup_template(self):
    self.assertEqual(self.response.status_code, 200)
    self.assertTemplateUsed(self.response, 'register/teacher_register.html')
    self.assertContains(self.response, "Teacher")
    self.assertNotContains(self.response, 'Students')
    self.assertEqual(
      self.view.func.__name__, teacher_register.as_view().__name__
    )

  def test_teacher_signup_form(self):
    teacher_user = User.objects.create_user(
      self.username, self.email, is_teacher=True
    )
    self.assertEqual(User.objects.all().count(), 1)
    self.assertEqual(User.objects.all()[0].username, self.username)
    self.assertEqual(User.objects.all()[0].email, self.email)
    self.assertTrue(teacher_user.is_teacher, True)
    self.assertFalse(teacher_user.is_student, True)


class LoginPageTest(TestCase):
  
  def setUp(self):
    url = reverse('login_view')
    self.response = self.client.get(url)
    self.view = resolve('/accounts/register/login/')
