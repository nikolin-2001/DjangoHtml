from django import forms
from .models import *

class AddShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['name', 'slug', 'descriprion', 'sex', 'price', 'size', 'images', 'firm', 'cat']
