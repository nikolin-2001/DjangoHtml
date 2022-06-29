from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import ShoesSerializer, JeansSerializer, TshirtSerializer, SweathirtsSerializer
from django.views.generic import ListView, CreateView


'''Фильтрация вещей'''

'''Для пагинатора'''
def show_category(request, cat_id):
    shoes = Shoes.objects.filter(cat_id=cat_id).order_by('-id')
    cats = Category.objects.all()
    paginator = Paginator(shoes, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if len(shoes) == 0:
        raise Http404()

    context = {'page_obj': page_obj,'shoes': shoes, 'cats': cats, 'cat_selected': cat_id}
    return render(request, 'myapi/index.html', context=context)

class ShoesProduct(ListView):
    paginate_by = 3
    model = Shoes
    template_name = 'myapi/index.html'
    context_object_name = 'posts'

def product_open(request, shoes_id):
    open = get_object_or_404(Shoes, pk=shoes_id)
    shoes = Shoes.objects.all().order_by('-id')
    context = {'shoes': shoes}
    return render(request, 'myapi/open.html', context)

    def show_open(request, shoes_id):
        return HttpResponse(f'Отображение категорий с id = {shoes_id}')

'''Привязка модели к файлу index.html'''
def index(request):
    shoes = Shoes.objects.all().order_by('-id')
    cats = Category.objects.all()
    paginator = Paginator(shoes, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'shoes': shoes, 'cats': cats, 'cat_selected': 0}
    return render(request, 'myapi/index.html', context)



'''Отображение обуви'''

class JeansViewSet(viewsets.ModelViewSet):
    queryset = Jeans.objects.all().order_by('name')
    serializer_class = JeansSerializer

class TshirtViewSet(viewsets.ModelViewSet):
    queryset = Tshirt.objects.all().order_by('name')
    serializer_class = TshirtSerializer

class SweatshirtsViewSet(viewsets.ModelViewSet):
    queryset = Sweatshirts.objects.all().order_by('name')
    serializer_class = SweathirtsSerializer

class CatalogCreate(CreateView):
    model = Catalog
    fields = ['text']
    def form_valid(self, form):
        self.object = form.save()
        return render(request, 'myapi/Catalog.html', context)


class PreviewCreate(CreateView):
    model = Preview
    fields = ['text']
    def form_valid(self, form):
        self.object = form.save()
        return render(request, 'myapi/preview_form.html', context)


