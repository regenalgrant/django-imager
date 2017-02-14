"""Testing imager images."""
from django.test import TestCase
from django.contrib.auth.models import User
from imager_images.models import Photo, Albums
from datetime import datetime
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


class AlbumFactory(factory.DjangoModelFactory):
    """Creating AlbumFactory to Albums class."""

    class Meta:
        """Setting Model to Albums class."""
        model = Albums
    title = factory.Sequence(lambda n: "photo title {}".format(n))


class PhotoTestCase(TestCase):
    """Creating Photo test class."""

    def setUp(self):
        """Setting up user."""
        self.user = UserFactory.create()
        self.user.set_password("1234")
        self.photo = PhotoFactory.build()
        self.photo.user = self.user
        self.photo.save()

    def test_photo_exist(self):
        """Setting up that photo exist."""
        self.assertEqual(Photo.objects.count(), 1)

    def test_photo_published(self):
        """Setting that photo is published."""
        self.assertTrue(self.photo.date_published)
        self.assertTrue(self.photo.title)
        self.assertFalse(self.photo.select_cover)

    def test_photo_is_private(self):
        """Setting that published status is private."""
        self.assertEqual(self.photo.published, "private")

    def test_photo_deletion(self):
        """Testing photo upon deletion."""
        self.photo.delete()
        self.assertTrue(Photo.objects.count() == 0)

    def test_photo_related_user(self):
        """Testing photo related to user."""
        self.assertEquals(self.photo.user, self.user)


class AlbumTestCase(TestCase):
    """Creating Album test class."""
    def setUp(self):
        """Creating setup for album."""
        self.user = UserFactory.create()
        self.user.set_password('1234')
        self.photo = PhotoFactory.create(user=self.user)
        self.album = AlbumFactory.create(user=self.user)
        self.photo.album.add(self.album)

    def test_album_published(self):
        """Testing album for published."""
        self.assertTrue(Albums.objects.first().published == "private")

    def test_album_related_user(self):
        """Testing album that relates to user."""
        self.assertEquals(self.album.user, self.user)

    def test_album_has_no_cover_default(self):
        """Testing album has no cover by default."""
        self.assertEquals(self.album.cover, None)

    def test_album_one_photo(self):
        """Testing album for one photo."""
        self.assertEquals(self.album.photos.count(), 1)
