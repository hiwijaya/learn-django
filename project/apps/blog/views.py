from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'blog.html')


def post(request):
    return HttpResponse('<h1>This is blog post</h1>')
