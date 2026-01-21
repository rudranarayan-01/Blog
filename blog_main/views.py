from django.http import HttpResponse
from django.shortcuts import render, redirect
from background.models import AboutModel
from blogs.models import Category, Blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

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
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:    
        form = RegistrationForm()
        
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Perform login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
        else:
            print(form.errors)
            
    form = AuthenticationForm()
    
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')