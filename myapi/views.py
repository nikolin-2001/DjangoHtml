from rest_framework import viewsets
from django.shortcuts import render
from .models import Shoes, Jeans, Tshirt, Sweatshirts, Catalog
from .serializers import ShoesSerializer, JeansSerializer, TshirtSerializer, SweathirtsSerializer
from django.views.generic.edit import CreateView

def index(request):
    shoes = Shoes.objects.all().order_by('-id')
    context = {'shoes': shoes}
    return render(request, 'myapi/index.html', context)

class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all().order_by('name')
    serializer_class = ShoesSerializer

class JeansViewSet(viewsets.ModelViewSet):
    queryset = Jeans.objects.all().order_by('name')
    serializer_class = JeansSerializer

class TshirtViewSet(viewsets.ModelViewSet):
    queryset = Tshirt.objects.all().order_by('name')
    serializer_class = TshirtSerializer

class SweatshirtsViewSet(viewsets.ModelViewSet):
    queryset = Sweatshirts.objects.all().order_by('name')
    serializer_class = SweathirtsSerializer

class PashalkaoneCreate(CreateView):
    model = Catalog
    fields = ['text']
    def form_valid(self, form):
        self.object = form.save()
        return render(request, 'myapi/Catalog.html', context)