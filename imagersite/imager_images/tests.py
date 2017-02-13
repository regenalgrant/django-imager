"""Testing imager images."""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import ImagerProfile
from imager_images.models import Photo, Albums
from ImageProfile.models import ImagerProfile
import factory

class UserFactory(factory.django.DjangoModelFactory):
    """Creating UserFactory to make users."""
    class Meta:
        """Setting Model to User class."""
        model = User # pulling from User class to build user factory

    username = factory.Sequence(
        lambda n: "user{}".format(n)
    )
    email = factory.Sequence(
        lambda n: "user{}@gmail.com".format(n)
    )


class PhotoFactory(factory.DjangoModelFactory):
    """Creating PhotoFactory to make Photos."""

    class Meta:
        """Settting Model to Photo class."""
        model = Photo # pulling from photo
    title = factory.Sequence(
        lambda n: "photo title {}".format(n)
    )
    select_cover = False
    date_uploaded = factory.LazyFunction(datetime.now)


class AlbumFactory(factor):
    """Creating AlbumFactory to Albums class."""

    class Meta:
        """Setting Model to Albums class."""
        model = Albums
    title = factory.Sequence(lambda n: "photo title {}".format(n)


class PhotoTestCase(TestCase):
    """Creating Photo test class."""

    def setUp(self):
        """Setting up fake user."""
        self.user = UserFactory.create()
        self.user.set_password("1234")
        self.photo = PhotoFactory.create()

    def test_photo_exist(self):
        """Setting up that photo exist."""
        self.assertEqual(Photo.objects.count(), 1)
