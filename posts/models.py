# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta: 
        verbose_name_plural = 'Categories'

class Products(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Categories, on_delete=True)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    user_post = models.ForeignKey(User, default=None, on_delete=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Products'