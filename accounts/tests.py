from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import User, Student, Teacher
from .views import HomeView

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
Test homepage
"""
class HomepageTests(SimpleTestCase):

  def setUp(self):
    url = reverse('home')
    self.response = self.client.get(url)

  def test_homepage_status_code(self):
    self.assertEqual(self.response.status_code, 200)

  def test_homepage_url_name(self):
    self.assertEqual(self.response.status_code, 200)

  def test_homepage_template(self):
    self.assertTemplateUsed(self.response, "home.html")

  def test_homepage_contains_correct_html(self):
    self.assertContains(self.response, "Homepage")

  def test_homepage_does_not_contain_incorrect_html(self):
    self.assertNotContains(self.response, "I am a student!")

  def test_homepage_url_resolve_homepageview(self):
    view = resolve('/')
    self.assertEqual(
      view.func.__name__, HomeView.as_view().__name__
    )
