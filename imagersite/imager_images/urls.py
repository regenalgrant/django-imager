
from django.conf.urls import url
from imager_images.views import (
    PhotoView,
    LibraryView,
    AlbumsView,
    SinglePhotoView,
    SingleAlbumsView,
    AddPhotoView,
    AddAlbumsView,
    EditSinglePhotoView,
    EditSingleAlbumsView,
)

urlpatterns = [
    url(r'^library/$', LibraryView.as_view(), name='library'),
    url(r'^photos$', PhotoView.as_view(), name='allphotos'),
    url(r'^photos/(?P<photoid>\d+)/$', SinglePhotoView.as_view(),
        name='singlephoto'),
    url(r'^albums$', AlbumsView.as_view(), name='albums'),
    url(r'^albums/(?P<albumsid>\d+)/$', SingleAlbumsView.as_view(),
        name='singlealbums'),
    url(r'^photos/add/$', AddPhotoView.as_view(), name='add_photo'),
    url(r'^albums/add/$', AddAlbumsView.as_view(), name='add_albums'),
    url(r'^albums/(?P<pk>\d+)/edit/$', EditSingleAlbumsView.as_view(),
        name='edit_albums'),
    url(r'^photos/(?P<pk>\d+)/edit/$', EditSinglePhotoView.as_view(),
        name='edit_photo'),
]
