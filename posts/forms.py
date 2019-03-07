
from django import forms
from . import models

class CreateAd(forms.ModelForm):
    class Meta:
        model = models.Products
        fields = ['name', 'category', 'price', 'description', 'image']

