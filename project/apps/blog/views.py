from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Blog',
        'banner': 'img/banner_blog.png',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
        ]
    }
    return render(request, 'index.html', context)


def post(request):
    return HttpResponse('<h1>This is blog post</h1>')
