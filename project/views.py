from django.http import HttpResponse


def home(request):
    title = '<h1>Home</h1>'
    subtitle = '<h2>Welcome to training-django</h2>'

    return HttpResponse(title + subtitle)
