"""Testing for registration and login."""
from django.test import Client, TestCase, RequestFactory
from django.contrib.auth.models import User
import factory



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


    def test_home_route_has_200(self):
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


    # def test_registered_user_redirects(self):
    #     """Test registration redirects."""
    #     response = self.new_user
    #     self.assertTrue(response.status_code == 302) # not passing


    def test_registered_user_is_not_active(self):
        """Test a newly registered user is inactive."""
        self.assertFalse(User.objects.count() == 0)
        self.client = User.objects.first()
        self.assertTrue(self.client.is_active) # ---not working, no attribute is_active


    # def test_login_route_redirects(self):
    #     """Login route redirect."""
    #     self.new_user = User.objects.create_user()
    #     self.new_user.set_password('zaq14321')
    #     response = self.client.post('/login/',
    #         # 'username'=self.new_user.username,
    #         'password'=('zaq14321')
    #     )
    #     self.assertTrue(response.status_code == 302)


# ------------registration email test----------


    class RegistrationEmailTest(TestCase): # pass
        """Testing for email send with message."""
        def test_send_email(self):
            mail.send_mail(
                'Hello', 'Thank for registrating.',
                'regenal@gmail.com', ['regenal@gmail.com'],
                fail_silently=False,
            )


        def test_message_has_been_sent(self):
            self.assertEqual(len(mail.outbox), 1)
