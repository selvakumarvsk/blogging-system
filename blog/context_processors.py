from .models import Category
from additional_blog.models import Social_media

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_media(request):
    social_media = Social_media.objects.all()
    return dict(social_media=social_media)