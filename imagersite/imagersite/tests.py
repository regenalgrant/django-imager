"""Testing for registration and login."""
from django.test import Client, TestCase, RequestFactory
from django.contrib.auth.models import User


class FrontEndTestCase(TestCase):
    """Test for registration and login."""
    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()

    def test_home_view_has_200(self):
        """Test for home view has a 200 status."""
        from .views import HomeView
        response = self.client.get('/')
        self.assertTrue(response.status_code == 200)
