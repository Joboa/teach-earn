from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView

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
      view.func.__name__, HomePageView.as_view().__name__
    )

