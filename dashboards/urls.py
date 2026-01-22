from django.urls import path
from . import views

urlpatterns = [
    # Dashboard URLs will be defined here
    path('', views.dashboard, name="dashboard"),
    path('categories/', views.categories, name="categories"),
]
