from datetime import timedelta
from io import StringIO

from django.core.urlresolvers import reverse
from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.utils import timezone
from django.contrib.auth.models import User

from pyladies_harare.models import Post


# Tests for URLs
class URLsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user("test_author", "pass1234")
        self.post = Post.objects.create(id=1, title='Test', summary='Test',
                                        text='Test', author=self.user, category_id=1)

    def test_get_homepage(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_get_homepage_no_slash(self):
        response = self.client.get("")
        self.assertEquals(response.status_code, 200)

    def test_get_home_url(self):
        response = self.client.get("/home/")
        self.assertEquals(response.status_code, 404)

    def test_get_about_page(self):
        response = self.client.get("/about/")
        self.assertEquals(response.status_code, 200)

    def test_get_about_no_slash(self):
        response = self.client.get("/about")
        self.assertEquals(response.status_code, 200)

    def test_get_about_url(self):
        response = self.client.get("/aboutus/")
        self.assertEquals(response.status_code, 200)

    def test_get_post_details_page(self):
        response = self.client.get("/post/1/")
        self.assertEquals(response.status_code, 200)

    def test_get_post_details_no_slash(self):
        response = self.client.get("/post/1")
        self.assertEquals(response.status_code, 301)

    def test_get_post_url_pk(self):
        response = self.client.get("/post/pk=1/")
        self.assertEquals(response.status_code, 404)

    def test_get_events_url(self):
        response = self.client.get("/events/")
        self.assertNotEquals(response.status_code, 200)

    def test_get_events_404_url(self):
        response = self.client.get("/events/")
        self.assertEquals(response.status_code, 404)


# Tests for Authentication
class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="test_user")
        self.user.set_password("pass1234")
        self.user.save()

    def test_login_success(self):
        response = self.client.login(username="test_user", password="pass1234")
        self.assertTrue(response)

    def test_login_wrong_username(self):
        response = self.client.login(username='john', password='pass1234')
        self.assertFalse(response)

    def test_login_wrong_password(self):
        response = self.client.login(username='test_user', password='smith')
        self.assertFalse(response)

    def test_login_user_does_not_exist(self):
        response = self.client.login(username='john', password='smith')
        self.assertFalse(response)

# Tests for Views
