"""Testing for registration and login."""
from django.test import Client, TestCase, RequestFactory
from django.contrib.auth.models import User


class FrontEndTestCase(TestCase):
    """Test for registration and login."""
    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()
        self.new_user = User.objects.create_user(
            username = 'regenal',
            email = 'regenal@gmail.com',
            password = 'zaq14321'
        )

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

    def test_registered_new_user(self):
        """Test a new user is created."""
        self.assertFalse(User.objects.count() == 0)
        self.new_user
        self.assertTrue(User.objects.count() == 1)

    # def test_registered_user_is_not_active(self):
    #     """Test a newly registered user is inactive."""
    #     self.user()
    #     self.client = User.objects.first()
    #     self.assertFalse(self.client.is_active) # ---not working, no attribute is_active
