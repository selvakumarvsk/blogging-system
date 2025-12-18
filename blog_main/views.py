from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    form = RegisterForm()
    context = {
        'forms' : form,
    }
    return render(request,'register.html', context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'forms' : form
    }
    return render(request, 'login.html',context)

def logout_page(request):
    auth.logout(request)
    return redirect('home')