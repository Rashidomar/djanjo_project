# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignUp,User
from django.contrib import  auth
from posts.models import Products,Categories
 
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
         form = SignUp(request.POST)
         if form.is_valid():
             user = form.save()
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password1')
             user = authenticate(username=username, password=password)
             login(request, user)
             return redirect('posts:index')
    else:
        form = SignUp()
    return render (request, 'accounts_tem/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
         form = AuthenticationForm(data=request.POST)  
         if form.is_valid():
             user = form.get_user()
             login(request, user)
             return redirect('posts:index')
    else:
        form = AuthenticationForm()
    return render (request, 'accounts_tem/login.html', {'form':form})

def profile(request):
    user_id = request.user.id
    products = Products.objects.filter(user_post_id=user_id).all()
    return render(request, 'accounts_tem/profile.html', {'products':products})

def dashboard(request):
    user_id = request.user.id
    products = Products.objects.filter(user_post_id=user_id).all()
    return render(request, 'accounts_tem/dashboard.html', {'products':products})



def logout_view(request):
    auth.logout(request)
    return redirect('posts:index')



    