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
