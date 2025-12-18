from django.shortcuts import get_object_or_404, redirect, render
from jupyterlab_server import slugify
from blog.models import Blog,Category
from .forms import CategoryForm,BlogForm,UserForm,EditUserForm
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    blog_count = Blog.objects.all().count()
    category_count = Category.objects.all().count()
    context = {
        'blog_count' : blog_count,
        'category_count' : category_count,
    }
    return render(request,'dashboard/dashboard.html',context)

def category_view(request):
    return render(request, 'dashboard/category_view.html')

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_view')
        else:
            print(form.errors)
    form = CategoryForm()
    context = {
        'forms' : form,
    }
    return render(request, 'dashboard/category_add.html', context)

def category_edit(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_view')
        else:
            print(form.errors)
    form = CategoryForm(instance=category)
    context = {
        'forms' : form,
        'category' : category,
    }
    return render(request, 'dashboard/category_edit.html', context)

def category_delete(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('category_view')

def post_view(request):
    post = Blog.objects.all()
    context = {
        'post' : post
    }
    return render(request, 'dashboard/post_view.html',context)

def post_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #temporarily
            post.author = request.user
            post.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('post_view')
        else:
            print('invalid ',form.errors)
    form = BlogForm()
    context = {
        'forms' : form
    }
    return render(request, 'dashboard/post_add.html',context)

def post_edit(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_view')
        else:
            print('invalid ',form.errors)
    form = BlogForm(instance=post)
    context = {
        'forms' : form,
        'post' : post,
    }
    return render(request, 'dashboard/post_edit.html',context)

def post_delete(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('post_view')

def user_view(request):
    user = User.objects.all()
    context = {
        'users' : user
    }
    return render(request, 'dashboard/user_view.html', context)

def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_view')
        else:
            print(form.errors)
    form = UserForm()
    context = {
        'forms' : form,
    }
    return render(request,'dashboard/user_add.html', context)

def user_edit(request,pk):
    user = get_object_or_404(User,pk=pk)
    if request.method == 'POST':
        form = EditUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_view')
        else:
            print(form.errors)
    form = EditUserForm(instance=user)
    context = {
        'forms' : form,
        'user' : user,
    }
    return render(request, 'dashboard/user_edit.html', context)

def user_delete(request,pk):
    user = get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('user_view')