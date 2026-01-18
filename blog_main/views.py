from django.http import HttpResponse
from django.shortcuts import render
from background.models import AboutModel
from blogs.models import Category, Blog

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by('-created_at')
    
    # Fetch about section
    try:
        about = AboutModel.objects.get()
    except AboutModel.DoesNotExist:
        about = None

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    
    # print(categories)
    
    return render(request, 'home.html', context)

def register(request):
    return render(request, 'register.html')