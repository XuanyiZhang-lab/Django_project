from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Photo, BlogPost

def home(request):
    return render(request, 'home.html')

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})

def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog_detail.html', {'post': post})
