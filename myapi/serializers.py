from rest_framework import serializers
from .models import Shoes, Jeans, Tshirt, Sweatshirts

class ShoesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shoes
        fields = ('name', 'descriprion', 'price')


class JeansSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Jeans
        fields = ('name', 'descriprion', 'price')


class TshirtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tshirt
        fields = ('name', 'descriprion', 'price')


class SweathirtsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sweatshirts
        fields = ('name', 'descriprion', 'price')