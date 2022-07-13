from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.urls import reverse_lazy
from rest_framework import viewsets
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from .serializers import *
from django.views.generic import ListView, CreateView
from django.contrib.auth.forms import UserCreationForm


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


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'myapi/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'myapi/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')
