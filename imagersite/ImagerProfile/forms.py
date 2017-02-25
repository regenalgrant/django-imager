from django import forms
from .models import ImagerProfile


class EditProfileForm(forms.ModelForm):
    """Form to edit profiles."""

    def __init__(self, *args, **kwargs):
        """Form fields."""
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields["First Name"] = forms.CharField(initial=self.instance.user.first_name)
        self.fields["Last Name"] = forms.CharField(initial=self.instance.user.last_name)
        self.fields["Email"] = forms.EmailField(initial=self.instance.user.email)
        del self.fields["user"]

    class Meta:
        """Exclusion principles."""

        model = ImagerProfile
        exclude = []
