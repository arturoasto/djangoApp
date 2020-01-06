from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'neil',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'today'
    },
    {
        'author': 'Jane Doe',
        'title': 'blog post 2',
        'content': 'Second post content',
        'date_posted': 'tomorrow'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
