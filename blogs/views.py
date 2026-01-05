from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def posts_by_category(request, category_id):
    # Logic to fetch posts by category_id
    print(category_id)
    return HttpResponse("Posts for category")