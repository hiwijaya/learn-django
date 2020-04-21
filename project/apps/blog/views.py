from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'title': 'Learn Django',
        'contributor': 'Happy Indra Wijaya'
    }
    return render(request, 'blog.html', context)


def post(request):
    return HttpResponse('<h1>This is blog post</h1>')
