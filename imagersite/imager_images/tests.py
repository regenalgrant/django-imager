from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse_lazy
from ImagerProfile.models import ImagerProfile
from imager_images.models import Photo, Albums
import factory





class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "Imgr User {}".format(n))
    email = factory.LazyAttribute(
        lambda x: "{}@datsite.com".format(x.username.replace(" ", ""))
    )


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo
    title = factory.Sequence(lambda n: "Photo {}".format(n))
    image_file = SimpleUploadedFile(name='reggie copy.jpg', content=open('imagersite/static/images/reggie copy.jpg', 'rb').read(), content_type='image/jpeg')


class AlbumsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Albums
    title = factory.Sequence(lambda n: "Albums {}".format(n))
    cover_image = SimpleUploadedFile(name='reggie copy.jpg', content=open('imagersite/static/images/reggie copy.jpg', 'rb').read(), content_type='image/jpeg')
    description = "Some Albums"


class ImageTestCase(TestCase):
    """Image Test Class."""

    def setUp(self):
        """User, photos, and albums setup for tests."""
        self.users = [UserFactory.create() for i in range(10)]
        self.photo = [ImageFactory.create() for i in range(10)]
        self.albums = [AlbumsFactory.create() for i in range(10)]

    def test_photo_title(self):
        """Test that photo has a title."""
        self.assertTrue("Photo" in Photo.objects.first().title)

    def test_photo_has_description(self):
        """Test that the photo description field can be assigned."""
        photo = Photo.objects.first()
        photo.description = "Works."
        photo.save()
        self.assertTrue(Photo.objects.first().description == "Works.")

    def test_photo_is_published(self):
        """photo should have a published field."""
        photo = Photo.objects.first()
        photo.published = 'public'
        photo.save()
        self.assertTrue(Photo.objects.first().published == "public")

    def test_photo_date_modified(self):
        """photo should have a date modified default."""
        photo = Photo.objects.first()
        self.assertTrue(photo.date_modified)

    def test_photo_date_uploaded(self):
        """photo should have a default date uploaded."""
        photo = Photo.objects.first()
        self.assertTrue(photo.date_uploaded)

    def test_photo_no_date_date_published(self):
        """Test that the photo does not have a date published before assignment."""
        photo = Photo.objects.first()
        self.assertFalse(photo.date_published)

    def test_photo_date_date_published(self):
        """Test that the photo has a date published after assignment."""
        photo = Photo.objects.first()
        photo.date_published = timezone.now
        self.assertTrue(photo.date_published)

    def test_photo_has_no_owner(self):
        """Test that photo has no owner."""
        photo = Photo.objects.first()
        self.assertFalse(photo.owner)

    def test_photo_has_owner(self):
        """Photo should have owner after assignment."""
        photo = Photo.objects.first()
        user1 = User.objects.first()
        photo.owner = user1.profile
        self.assertTrue(photo.owner)

    def test_owner_has_photo(self):
        """Owner should be associated with the photo."""
        photo = Photo.objects.first()
        user1 = User.objects.first()
        photo.owner = user1.profile
        photo.save()
        self.assertTrue(user1.profile.photo.count() == 1)

    def test_two_photos_have_owner(self):
        """Two pics should have same owner."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.assertTrue(photo1.owner == user1.profile)
        self.assertTrue(photo2.owner == user1.profile)

    def test_owner_has_two_photos(self):
        """Test that owner has two photo."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.assertTrue(user1.profile.photo.count() == 2)

    def test_photo_has_no_albums(self):
        """Test that the photo is in an albums."""
        photo = Photo.objects.first()
        self.assertTrue(photo.albums_of_photos.count() == 0)

    def test_photo_has_albums(self):
        """Test that the photo is in an albums."""
        photo = Photo.objects.first()
        albums1 = Albums.objects.first()
        photo.albums_of_photos.add(albums1)
        self.assertTrue(photo.albums_of_photos.count() == 1)

    def test_albums_has_no_photo(self):
        """Test that an albums has no photo before assignemnt."""
        albums1 = Albums.objects.first()
        self.assertTrue(albums1.images.count() == 0)

    def test_albums_has_photo(self):
        """Test that an albums has an photo after assignemnt."""
        photo = Photo.objects.first()
        albums1 = Albums.objects.first()
        photo.albums_of_photos.add(albums1)
        self.assertTrue(photo.albums_of_photos.count() == 1)

    def test_two_photos_have_albums(self):
        """Test that two photos have same albums."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        albums1 = Albums.objects.first()
        photo1.albums_of_photos.add(albums1)
        photo2.albums_of_photos.add(albums1)
        photo1.save()
        photo2.save()
        self.assertTrue(photo1.albums_of_photos.all()[0] == albums1)
        self.assertTrue(photo2.albums_of_photos.all()[0] == albums1)

    def test_albums_has_two_photos(self):
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        albums1 = Albums.objects.first()
        photo1.albums_of_photos.add(albums1)
        photo2.albums_of_photos.add(albums1)
        photo1.save()
        photo2.save()
        self.assertTrue(albums1.images.count() == 2)

    def test_photo_has_two_albums(self):
        """Test that an photo has two albums."""
        photo1 = Photo.objects.first()
        albums1 = Albums.objects.all()[0]
        albums2 = Albums.objects.all()[1]
        photo1.albums_of_photos.add(albums1)
        photo1.albums_of_photos.add(albums2)
        photo1.save()
        self.assertTrue(photo1.albums_of_photos.count() == 2)

    def test_albums_title(self):
        """Test that the albums has a title."""
        self.assertTrue("Albums" in Albums.objects.first().title)

    def test_albums_has_description(self):
        """Test that the albums description field can be assigned."""
        albums = Albums.objects.first()
        albums.description = "This is a good albums."
        albums.save()
        self.assertTrue(Albums.objects.first().description == "This is a good albums.")

    def test_albums_has_published(self):
        """Test the albums publisalbumshed field."""
        albums = Albums.objects.first()
        albums.published = 'public'
        albums.save()
        self.assertTrue(Albums.objects.first().published == "public")

    def test_albums_date_modified(self):
        """Test that the albums has a date modified default."""
        albums = Albums.objects.first()
        self.assertTrue(albums.date_modified)

    def test_albums_date_created(self):
        """Test that the albums has a date uploaded default."""
        albums = Albums.objects.first()
        self.assertTrue(albums.date_uploaded)

    def test_albums_no_date_date_published(self):
        """Test that the albums does not have a date published before assignment."""
        albums = Albums.objects.first()
        self.assertFalse(albums.date_published)

    def test_albums_date_date_published(self):
        """Test that the albums has a date published after assignment."""
        albums = Albums.objects.first()
        albums.date_published = timezone.now
        self.assertTrue(albums.date_published)

    def test_albums_has_no_owner(self):
        """Test that albums has no owner."""
        albums = Albums.objects.first()
        self.assertFalse(albums.owner)

    def test_albums_has_owner(self):
        """Albums should have an owner after assignment."""
        albums = Albums.objects.first()
        user1 = User.objects.first()
        albums.owner = user1.profile
        self.assertTrue(albums.owner)

    def test_owner_has_albums(self):
        """Test that the owner has the albums."""
        albums = Albums.objects.first()
        user1 = User.objects.first()
        albums.owner = user1.profile
        albums.save()
        # import pdb; pdb.set_trace()
        self.assertTrue(user1.profile.albums.count() == 1)

    def test_two_albums_have_owner(self):
        """Two albums should have same owner."""
        albums1 = Albums.objects.all()[0]
        albums2 = Albums.objects.all()[1]
        user1 = User.objects.first()
        albums1.owner = user1.profile
        albums2.owner = user1.profile
        albums1.save()
        albums2.save()
        self.assertTrue(albums1.owner == user1.profile)
        self.assertTrue(albums2.owner == user1.profile)

    def test_owner_has_two_albums(self):
        """Owner should have two albums."""
        albums1 = Albums.objects.all()[0]
        albums2 = Albums.objects.all()[1]
        user1 = User.objects.first()
        albums1.owner = user1.profile
        albums2.owner = user1.profile
        albums1.save()
        albums2.save()
        self.assertTrue(user1.profile.albums.count() == 2)

    def test_logged_in_user_has_library(self):
        """A logged in user has a library."""
        user = UserFactory.create()
        user.save()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("library"))
        self.assertTrue(response.status_code == 200)

    def test_logged_in_user_sees_their_albums(self):
        """Logged in user should see their albums."""
        user = UserFactory.create()
        albums1 = Albums.objects.first()
        albums2 = Albums.objects.all()[1]
        user.profile.albums.add(albums1)
        user.profile.albums.add(albums2)
        user.save()
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("library"))
        self.assertTrue(albums1.description in str(response.content))

    def test_photo_view(self):
        """Test photos on photo view."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.client.force_login(user1)
        response = self.client.get(reverse_lazy("allphotos"))
        self.assertTrue(photo1.image_file.url in str(response.content))

    def test_Single_Photo_view(self):
        """Test photo on single photo view."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        self.client.force_login(user1)
        response = self.client.get(reverse_lazy("singlephoto", kwargs={'photoid': photo1.id}))
        self.assertTrue(photo1.image_file.url in str(response.content))

    def test_logged_in_user_sees_their_albums_on_albums(self):
        """Logged in user should see their albums."""
        user = UserFactory.create()
        albums1 = Albums.objects.first()
        albums2 = Albums.objects.all()[1]
        user.profile.albums.add(albums1)
        user.profile.albums.add(albums2)
        user.save()
        self.client.force_login(user)
        response = self.client.get(reverse_lazy("singlealbums", kwargs={'albumsid': albums1.id}))
        self.assertTrue(albums1.description in str(response.content))

    def test_logged_in_user_does_not_see_other_albums(self):
        """Logged in user should see their albums."""
        user1 = UserFactory.create()
        user2 = UserFactory.create()
        albums1 = Albums.objects.first()
        albums2 = Albums.objects.all()[1]
        user1.profile.albums.add(albums1)
        user1.profile.albums.add(albums2)
        user1.save()
        user2.save()
        self.client.force_login(user2)
        response = self.client.get('/images/albums/' + str(albums1.id), {"follow": True}, follow=True)
        self.assertTrue(response.status_code == 403)

    def test_single_photo_view_returns_404(self):
        """Test photo on single photo view."""
        photo1 = Photo.objects.all()[0]
        photo2 = Photo.objects.all()[1]
        user1 = User.objects.first()
        user2 = UserFactory.create()
        photo1.owner = user1.profile
        photo2.owner = user1.profile
        photo1.save()
        photo2.save()
        user2.save()
        self.client.force_login(user2)
        response = self.client.get(reverse_lazy("singlephoto", kwargs={'photoid': photo1.id}))
        self.assertTrue(response.status_code == 403)
