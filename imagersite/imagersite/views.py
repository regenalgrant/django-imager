from random import randint
from django.shortcuts import render
from imager_images.models import Photo
from django.conf import settings

from django.views.generic import TemplateView

class HomeView(TemplateView): # ensure update template path
    """Creating HomeView template."""

    template_name = "home.html"

    def get_context_data(self):
        """View for the home page."""
        photos = Photo.objects.all()
        if photos:
            idx = randint(0, photos.count() - 1)
            random_picture = photos[idx]
            img_url = random_picture.image_file.url
        else:
            img_url = settings.STATIC_URL + 'images/reggie copy.jpg'
        context = {'img_url': img_url}
        return context
