# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Products,Categories


# Create your views here.

def index(request):
    categories = Categories.objects.all()
    return render(request, 'posts_tem/index.html', {'categories': categories}) 

def product_category(request):
    categories = Categories.objects.all()
    return render(request, 'posts_tem/product_catergory.html', {'categories': categories})


@login_required(login_url="/accounts/login/")
def upload(request):
    if request.method == 'POST':
         form = forms.CreateAd(request.POST,request.FILES)
         if form.is_valid():
             new_post = form.save(commit=False)
             new_post.user_post = request.user
             new_post.save()
             return redirect('posts:index')
    else:
        form = forms.CreateAd()
    return render(request, 'posts_tem/upload.html', {'form': form})


def product_detail(request, cat_id):
    products = Products.objects.filter(category_id = cat_id).all()
    return render(request, 'posts_tem/detail.html', {'products':products})


def product_delete(request, product_id):
    product = Products.objects.get(pk=product_id)
    product.delete()
    return redirect('posts:index')



