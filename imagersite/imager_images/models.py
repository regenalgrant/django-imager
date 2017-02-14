"""Creating two models of photo and album."""


from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


PUBLISH_OPTIONS = [("private", "Private"),
                   ("shared", "Shared"),
                   ("public", "Public")]


@python_2_unicode_compatible
class Photo(models.Model):
    """Creating class called photo from model.Models."""
    user = models.OneToOneField(
        User,
        related_name='photo',
        null=False,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=255, blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)
    select_cover = models.BooleanField(default=False)
    published = models.CharField(
        max_length=7,
        choices=PUBLISH_OPTIONS,
        default='private',
        blank=True
    )
    upload = models.ImageField(upload_to='user_photos', blank=True, null=True) # path to file


    def __str__(self):
        return "{} photo has been uploaded".format(self.user)


@python_2_unicode_compatible
class Albums(models.Model):
    """Creating the class called album from models.Model."""
    user = models.OneToOneField(
        User,
        related_name='album',
        on_delete=models.CASCADE,
    )
    photos = models.ManyToManyField(
        Photo,
        related_name="album",
    )
    title = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=255, blank=True)
    date_created = models.DateField(auto_now=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.CharField(
        max_length=7,
        choices=PUBLISH_OPTIONS,
        default='private',
        blank=True
    )

    @property
    def cover(self):
        """Set image as a cover."""
        return self.photos.filter(select_cover=True).last()

    def __str__(self):
        return "album created for {}".format(self.user.username)
