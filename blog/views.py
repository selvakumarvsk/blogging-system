from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Category,Blog
from additional_blog.models import About
from django.db.models import Q

# Create your views here.
def homepage(request):
    # category = Category.objects.all()         # because we used context_processors 
    featured_post = Blog.objects.filter(is_featured=True)
    post = Blog.objects.filter(is_featured=True,status="Published")
    draft_post = Blog.objects.filter(status="Draft")
    about = About.objects.all()
    context={
        # 'categories' : category,
        'featured_posts' : featured_post,
        'posts' : post,
        'draft_posts' : draft_post,
        'about' : about,
    }
    return render(request, 'home-blogs.html',context)

def category(request,pk):
    post = Blog.objects.filter(category=pk,status="Published")
    category = Category.objects.get(pk=pk)
    context={
        'posts' : post,
        'category' : category
    }
    return render(request, 'category.html',context)

def single_blog(request,slug):
    post = Blog.objects.filter(slug=slug)
    about = About.objects.all()
    context={
        'posts' : post,
        'about' : about,
    }
    return render(request, 'single_blog.html',context)

def search(request):
    keyword = request.GET.get('keyword')
    blog = Blog.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword) | Q(blog_body__icontains=keyword), status = 'Published')
    context={
        'blogs' : blog,
        'keyword' : keyword,
    }
    return render(request, 'search.html', context)