from django.shortcuts import render
from django.template import loader
from django.conf import setting import MEDIA_URL

def home_view(request):
    """The Home View."""
    import random
    img_list = Image.object.all()
    if not i(mg list) == 0
        img_url =""/media
        else


    return render(request,
                "imagersite/home.html",
                 {"yo!": "yo!"}
                 )
