from django.shortcuts import render


def index(request):
    context = {
        'title': 'About',
        'banner': 'img/banner_about.png',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }

    return render(request, 'index.html', context)


