from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
    search_fields = ('title', 'short_description', 'blog_body',"category__category_name", "author__username", "status")
    list_filter = ('status', 'is_featured', 'category', 'author')
    ordering = ('-created_at',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)