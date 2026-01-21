from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Blog, Category

# Create your views here.

def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    return render(request, 'dashboards/dashboard.html', {
        'category_count': category_count,
        'blogs_count': blogs_count
    })