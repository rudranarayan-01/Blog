from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category, Comment
from django.db.models import Q

# Create your views here.

def posts_by_category(request, category_id):
    # Logic to fetch posts by category_id
    posts = Blog.objects.filter(status="Published", category=category_id)
    
    # We use try-except when we want custom action on exception
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    
    # we can use get_object_or_404 as well for redirect to 404 error page
    # category = get_object_or_404(Category, pk=category_id)
    
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    
    # Handling comment
    comment = Comment.objects.filter(blog=single_blog)
    
    context = {
        'single_blog': single_blog,
        'comments': comment,
    }
    return render(request, 'blogs.html', context)

def search_blogs(request):
    keyword = request.GET.get('keyword', '')
    print("Keyword:", keyword)
    if keyword:
        blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    else:
        blogs = Blog.objects.none()  # Return an empty queryset if no keyword is provided

    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)