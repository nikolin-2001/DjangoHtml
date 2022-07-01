from rest_framework import serializers
from .models import *

class ShoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoes
        fields = ('name', 'slug', 'descriprion', 'sex', 'price', 'size', 'images', 'firm', 'cat')
