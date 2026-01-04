from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    # print(categories)
    
    return render(request, 'home.html', context)
