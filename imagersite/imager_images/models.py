"""Creating two models of photo and album."""


from django.db import models
from django.contrib.auth import User
from django.utils.encoding import python_2_unicode_compatible


PUBLISH_OPTIONS = [("private", "Private"),
                   ("shared", "Shared"),
                   ("public", "Public")]


@python_2_unicode_compatible
class Photo(models.Model):
    """Creating class called photo from model.Models."""
    user = models.OneToOneField(
        User,
        related_name="photo",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=30, blank=True)
    description = models.CharField(blank=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(auto_now_add=True)
    published = models.CharField(
        max_length=7,
        choices=PUBLISH_OPTIONS
        default='private',
        blank=True
        )
    upload = models.ImageField(upload_to='user_photos') # path to file

    def __str__(self):
        return "{} photo has been uploaded".format(self.user)
