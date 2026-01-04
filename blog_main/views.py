from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status="Published").order_by('-created_at')
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
    }
    
    # print(categories)
    
    return render(request, 'home.html', context)
