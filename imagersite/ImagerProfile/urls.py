from django.conf.urls import url
from ImagerProfile.views import (
    EditProfileView,
    ProfileView,
    OtherUserProfileView
)



urlpatterns = [
    url(r'^edit$', EditProfileView.as_view(), name='edit_profile'),
    url(r'^$', ProfileView.as_view(), name="profile"),
    url(r'^(?P<username>\w+)/$', OtherUserProfileView.as_view(), name="user_profile"),
]
