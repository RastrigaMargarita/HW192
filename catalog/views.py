from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from catalog.models import Usercontact, Product


class Index(TemplateView):
    """Отображаем первую страницу, выводим первые три продукта в карточки, если база данных не пуста"""
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['product_list'] = Product.objects.all()[:3]
        return context_data


class UsercontactCreateView(CreateView):
    """Передаем в базу данных то что прислал пользователь"""
    model = Usercontact
    fields = ('name', 'phone', 'message',)
    success_url = reverse_lazy('index')


class ProductDetailView(DetailView):
    """Показывам карточку товара"""
    model = Product
    template_name = 'catalog/product_detail.html'
