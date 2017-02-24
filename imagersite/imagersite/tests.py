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

class RegistrationTestCase(TestCase):
    """Setup Registration test case."""
    def setUp(self):
        """Set up response for registration test case."""
        self.response = self.client.post('/registration/register/', {
            'username': 'regenal',
            'email': 'regenal@gmail.com',
            'password1': '1qaz2wsx',
            'password2': '1qaz2wsx'
            }, follow=True)
        self.new_user = User.objects.create_user(
            username = 'regenal',
            email = 'regenal@gmail.com',
            password = 'zaq14321'
            )

    def test_registered_new_user(self):
        """Test a new user is created."""
        count = User.objects.count()
        self.new_user2 =  User.objects.create_user(
            username = 'regenal2',
            email = 'regenal@gmail.com',
            password = 'zaq14321'
            )
        self.assertTrue(User.objects.count() == count + 1)


    def test_registered_user_redirects(self):
        """Test registration redirects."""
        self.assertTrue(self.response.status_code == 200) # not passing


    def test_registered_user_is_not_active(self):
        """Test a newly registered user is inactive."""
        self.client = User.objects.first()
        self.assertTrue(self.client.is_active) # ---not working, no attribute is_active


    def test_login_route_redirects(self):
        """Login route redirect."""
        self.new_user = User.objects.create_user("regenal3")
        self.new_user.set_password('zaq14321')
        self.new_user.save()
        response = self.client.post('/login/',
            {'username':"regenal3",
            'password':'zaq14321'}
        )
        self.assertTrue(response.status_code == 302)


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
