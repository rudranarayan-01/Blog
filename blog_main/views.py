from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-created_at')[:5]
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
    }
    
    # print(categories)
    
    return render(request, 'home.html', context)
