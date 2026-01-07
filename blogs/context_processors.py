from .models import Category
from background.models import SocialLinks

def get_categories(request):
    from blogs.models import Category
    categories = Category.objects.all()
    return {'categories': categories}

def get_social_links(request):
    social_links = SocialLinks.objects.all()
    return {'social_links': social_links}