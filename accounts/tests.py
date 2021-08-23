from django.test import TestCase
from .models import User, Student, Teacher

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