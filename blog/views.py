from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, slug):
    return render_to_response('post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })


def about(request):
    return render(request, 'about.html', {})