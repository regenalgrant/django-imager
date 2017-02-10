from django.test import TestCase
from django.contrib.auth.models import User
from .models import ImagerProfile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(
        lambda number: "{} bob".format(number)
    )
    email = factory.LazyAttribute(
        lambda x: "{}@gmail.com".format(x.username)
    )


class ProfileTestCase(TestCase):
    """Profile Model being test with this class."""

    def setUp(self):
        """Setup profile to test."""
        self.users = [UserFactory.create() for i in range(20)]

    def test_reciever(self):
        """Test new users are made for profile."""
        self.assertEqual(ImagerProfile.objects.count(), 20)

    def test_user_has_profile_attached(self):
        """Testing for Profiles attached Users."""
        bob = self.users[2]
        self.assertTrue(hasattr(bob, "profile"))
        self.assertIsInstance(bob.profile, ImagerProfile)

    def test_profile_associated_actual_users(self):
        """Testing for profile Associated with real users."""
        a_profile = ImagerProfile.objects.first()
        self.assertTrue(hasattr(a_profile, "user"))
        self.assertIsInstance(a_profile.user, User)

    # def test_active_user(self):
    #     """Testing the user is active."""
    #     self.assert_true(user.is_active)

        def test_profile_str_is_user_username(self):
            self.user.save()
            profile = ImagerProfile.objects.get(user=self.user)
            self.assertEqual(str(profile), self.user.username)

#  --------------------TESTVIEWS---------------------

    def test_profile_views(self):
        """Test profile view status code."""
        from image_profile.view import profile_view
        req = self.request.get("/profile")
        self.asserTempplateUsed(response, 'imager_profile/detail.html')

    def test_home_view_status(self):
        """Test home view is assessible."""
        from imagersite.views import home_view
        req = self.request.get("/")
        response = home_view(req)
        self.assertEqual(response.status_code, 200)

    def home_route_uses_right_template(self):
        """Test that home route uses the expected template."""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'imagersite/home.html')

    def test_login_view_status(self):
        """Test login view is accesible."""
        from fjango.contrib.auth.views import login
        req = self.request.get('/')
        response = login(req)
        self.assertTemplatedUsed(response.staus_code, 200)

    def test_login_route_uses_right_template(self):
        """Test that the login route uses the expected template."""
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_register_view_status(self):
        """Test register view status code is 200."""
        from registration
