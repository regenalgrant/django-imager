from django.shortcuts import render
from django.template import loader

def home_view(request):
    """The Home View."""
    return render(request,
                "imagersite/home.html",
                 {"yo!": "yo!"}
                 )

def test_views(request, num=None, word=None):
    return render(request,
                "imagersite/home.html",
                 {"yo!": "yo!"
                  "num": num,
                  "word": word}
                 )
