
from django.shortcuts import render
from django.contrib.auth.models import User
from imager_images.models import Photo
from ImagerProfile.models import ImagerProfile
from ImagerProfile.forms import EditProfileForm
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, UpdateView
from django.shortcuts import redirect


class ProfileView(TemplateView):
    """Return the Profile View inheriting from TemplateView."""

    template_name = 'ImagerProfile/profile.html'

    def get_context_data(self, username=None):
        """Get profiles and return them."""
        if self.request.user.is_authenticated():
            public_images = self.request.user.profile.photo.filter(published='public').count()
            private_images = self.request.user.profile.photo.filter(published='private').count()
            profile = self.request.user.profile
            return {'profile': profile,
                    'public_images': public_images,
                    'private_images': private_images}
        else:
            error_message = "You're not signed in."
            return {'error': error_message}


class OtherUserProfileView(TemplateView):
    """Return other user profile views."""

    template_name = 'ImagerProfile/profile.html'

    def get_context_data(self, username):
        """View for other users profile's."""
        user = User.objects.get(username=username)
        profile = user.profile
        public_images = profile.photo.filter(published='public').count()
        private_images = profile.photo.filter(published='private').count()
        if self.request.user.is_authenticated():
            return {'profile': profile,
                    'public_images': public_images,
                    'private_images': private_images}
        else:
            error_message = "You're not signed in."
            return {'error': error_message}

    def get_context_data(self, username):
        """View for other users profile's."""
        user = User.objects.get(username=username)
        profile = user.profile
        public_images = profile.photo.filter(published='public').count()
        private_images = profile.photo.filter(published='private').count()
        return {'profile': profile,
                'public_images': public_images,
                'private_images': private_images}


class EditProfileView(LoginRequiredMixin, UpdateView):
    """Edit the authenticated users profile."""

    template_name = 'ImagerProfile/edit_profile.html'
    model = ImagerProfile
    form_class = EditProfileForm

    def get_object(self):
        """Get the user profile object."""
        return self.request.user.profile

    def form_valid(self, form):
        """Save model forms to database."""
        self.object = form.save()
        self.object.user.first_name = form.cleaned_data['First Name']
        self.object.user.last_name = form.cleaned_data['Last Name']
        self.object.user.email = form.cleaned_data['Email']
        self.object.user.save()
        self.object.save()
        return redirect('profile')
