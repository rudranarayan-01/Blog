from .models import Category

def get_categories(request):
    from blogs.models import Category
    categories = Category.objects.all()
    return {'categories': categories}