from django.shortcuts import render
from .models import *
# Create your views here.

def hello(request):
    context = {
        'message': 'Hello, Pythonanywhere',
    }
    return render(request, 'hello_app/index.html', context)


def input(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        Post.objects.create(name=name, message=message)
    return render(request, 'hello_app/input.html')


def output(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'hello_app/output.html', context)