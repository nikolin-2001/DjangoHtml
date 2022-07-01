from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from django.views.generic import ListView, CreateView


def show_category(request, cat_id):
    shoes = Shoes.objects.filter(cat_id=cat_id).order_by('-id')
    cats = Category.objects.all()
    paginator = Paginator(shoes, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if len(shoes) == 0:
        raise Http404()

    context = {'page_obj': page_obj,'shoes': shoes, 'cats': cats, 'cat_selected': cat_id}
    return render(request, 'myapi/index.html', context=context)

class ShoesProduct(ListView):
    paginate_by = 9
    model = Shoes
    template_name = 'myapi/index.html'
    context_object_name = 'posts'

def product_open(request, shoes_slug):
    open = get_object_or_404(Shoes, slug=shoes_slug)
    shoes = Shoes.objects.all().order_by('-id')
    context = {'shoes': shoes, 'open': open, 'cat_selected': open.cat_id}
    return render(request, 'myapi/open.html', context)

'''Привязка модели к файлу index.html'''
def index(request):
    shoes = Shoes.objects.all().order_by('-id')
    cats = Category.objects.all()
    paginator = Paginator(shoes, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj, 'shoes': shoes, 'cats': cats, 'cat_selected': 0}
    return render(request, 'myapi/index.html', context)

class PreviewCreate(CreateView):
    model = Preview
    fields = ['text']
    def form_valid(self, form):
        self.object = form.save()
        return render(request, 'myapi/preview_form.html', context)


