"""Testing for registration and login."""
from django.test import Client, TestCase, RequestFactory
from django.contrib.auth.models import User
from django

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

    def test_home_route_has_200(self):
        """Test for route has 200 status."""
        from .views import HomeView
        req = self.request.get('/anything')
        response = self.client.get('/')
        self.assertTrue(response.status_code == 200)

    def test_login_route(self):
        """Test for a 200 status route on login."""
        response = self.client.get('/login/')
        self.assertTrue(response.status_code == 200)

    def test_registered_user(self):
        """Test a user is created."""
        self.register_user()
        self.assertTrue(User.objects.count() == 0)
        self.assertTrue(User.objects.count() == 1)
        pass
