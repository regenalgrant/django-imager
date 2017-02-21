from imager_images.models import Photo
from django.views.generic.base import TemplateView


class HomeView(TemplateView): # ensure update template path
    """Creating HomeView template."""
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            search = Photo.objects.filter(published="public").order_by('?')[0] # filtering for something
            context['pre_selected_photo'] = search # adding the search to my key dictionary
        except IndexError: # using as default
            context['pre_selected_photo'] = "/static/images/vic.jpg"
        return context
