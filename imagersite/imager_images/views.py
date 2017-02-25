from django.http import Http404
from django.http.response import HttpResponseForbidden
from django.views.generic import ListView, CreateView, UpdateView
from .forms import PhotoForm, AlbumsForm, EditPhotoForm, EditAlbumsForm
from ImagerProfile.models import ImagerProfile
from imager_images.models import Photo, Albums
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.urls import reverse_lazy


class LibraryView(ListView):
    """"Return the libraryView inheriting from ListView."""

    template_name = 'library.html'

    def get_context_data(self):
        """Get albums and photos and return them."""
        profile = ImagerProfile.active.get(user__username=self.request.user.username)
        photos = profile.photo.all()
        albums = profile.albums.all()
        username = self.request.user.username
        return {'photos': photos, 'profile': profile, 'albums': albums, 'username': username}

    def get_queryset(self):
        """."""
        return {}


class PhotoView(ListView):

    model = Photo
    template_name = 'imager_images/photos.html'

    def get_context_data(self):
        photos = Photo.objects.all()
        return {'photos': photos}


class SinglePhotoView(ListView):
    """View a single photo on a page."""
    model = Photo
    template_name = 'single_photo.html'

    def get_context_data(self):
        photo = Photo.objects.filter(id=int(self.kwargs['photoid'])).first()
        if photo and photo.owner:
            if photo.owner.user.username == self.request.user.username:
                return {'photo': photo}
        return {}

    def get(self, request, *args, **kwargs):
        """Get method to return."""
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        if context:
            return self.render_to_response(context)
        else:
            return HttpResponseForbidden()


class AlbumsView(ListView):
    """Return the AlbumsView inheriting from ListView."""
    model = Albums
    template_name = 'library.html'

    def get_context_data(self):
        """Get albums and return them."""
        albums = Albums.objects.all()
        return {'albums': albums}


class SingleAlbumsView(LoginRequiredMixin, ListView):
    """Return the AlbumsView inheriting from ListView."""
    model = Albums
    template_name = 'single_albums.html'

    def get_context_data(self):
        """Get albums and return them."""
        albums = Albums.objects.get(id=int(self.kwargs['albumsid']))
        if albums.owner.user.username == self.request.user.username or albums.published == 'public':
            return {'albums': albums}
        return {}

    def get(self, request, *args, **kwargs):
        """Get method to return."""
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        if context:
            return self.render_to_response(context)
        else:
            return HttpResponseForbidden()


class AddPhotoView(CreateView):
    """Class based view for creating photos."""

    model = Photo
    form_class = PhotoForm
    template_name = 'add_photo.html'

    def form_valid(self, form):
        photo = form.save()
        photo.owner = self.request.user.profile
        photo.date_uploaded = timezone.now()
        photo.date_modified = timezone.now()
        if photo.published == "public":
            photo.published_date = timezone.now()
        photo.save()
        return redirect('library')


class AddAlbumsView(CreateView):
    """Class based view for creating photos."""

    model = Albums
    form_class = AlbumsForm
    template_name = 'add_albums.html'

    def form_valid(self, form):
        albums = form.save()
        albums.owner = self.request.user.profile
        albums.date_uploaded = timezone.now()
        albums.date_modified = timezone.now()
        if albums.published == "public":
            albums.published_date = timezone.now()
        albums.save()
        return redirect('library')


class EditSingleAlbumsView(LoginRequiredMixin, UpdateView):
    """Edit an albums."""

    login_required = True
    success_url = reverse_lazy('library')
    template_name = 'edit_albums.html'
    model = Albums
    form_class = EditAlbumsForm

    def get_form(self):
        """Retrieve form and customize some fields."""
        form = super(EditSingleAlbumsView, self).get_form()
        form.fields['cover_image'].queryset = self.request.user.profile.photo.all()
        # form.fields['images'].queryset = self.request.user.profile.photo.all()
        return form

    def user_is_user(self, request):
        """Test if albums's owner is current user."""
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.owner.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        """If user owns albums let them do stuff."""
        if not self.user_is_user(request):
            return HttpResponseForbidden()
        return super(EditSingleAlbumsView, self).dispatch(
            request, *args, **kwargs)


class EditSinglePhotoView(LoginRequiredMixin, UpdateView):
    """Edit a photo."""

    login_required = True
    success_url = reverse_lazy('library')
    template_name = 'edit_photo.html'
    model = Photo
    form_class = EditPhotoForm
    form_class.Meta.exclude.append('photo')

    def user_is_user(self, request):
        """Test if albums's owner is current user."""
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.owner.user == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        """If user doesn't own albums, raise 403, else continue."""
        if not self.user_is_user(request):
            return HttpResponseForbidden()
        return super(EditSinglePhotoView, self).dispatch(
            request, *args, **kwargs)
