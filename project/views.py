from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    context = {
        'title': 'Home',
        'banner': 'img/banner_home.png',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }

    return render(request, 'index.html', context)
