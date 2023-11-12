from datetime import datetime

from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.forms import ProductForm, VersionForm
from catalog.models import Usercontact, Product, Version


class Index(TemplateView):
    """Отображаем первую страницу, выводим первые три продукта в карточки, если база данных не пуста"""
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['product_list'] = Product.objects.all()
        version_data = Version.objects.all()

        for product in context_data['product_list']:
            product.active_version_number = ""
            product.active_version_name = ""
            for version in version_data:
                if version.current_version is True and (version.product.slug == product.slug):
                    product.active_version_number = version.nomer
                    product.active_version_name = version.version_title

        return context_data


class UsercontactCreateView(CreateView):
    """Передаем в базу данных то что прислал пользователь"""
    model = Usercontact
    fields = ('name', 'phone', 'message',)
    success_url = reverse_lazy('index')


class ProductDetailView(DetailView):
    """Показываем карточку товара"""
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        version_list = Version.objects.filter(product=context_data['object'])

        context_data['version_list'] = version_list
        return context_data


class ProductUpdateView(UpdateView):
    """Вью для обновления данных продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.last_changing_date = datetime.now()
            new_product.save()
            return super().form_valid(form)


class ProductCreateView(CreateView):
    """Вью для создания нового продукта"""
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        print('sldkfj')
        if form.is_valid():
            new_product = form.save()
            new_product.slug = slugify(new_product.title)
            new_product.seller = self.request.user
            new_product.save()

            return super().form_valid(form)


class ProductDeleteView(DeleteView):
    """Вью для удаления продукта"""
    model = Product
    success_url = reverse_lazy('index')

class VersionCreateView(CreateView):
    """Вью для создания новой версии продукта"""
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_create.html'
    success_url = reverse_lazy('index')



    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        print('ja context data')
        return data

    def form_valid(self, form):
        print("ja valid")
        if form.is_valid():
            new_version = form.save(commit=False)
            print(Product.objects.get(slug = self.kwargs['slug']))
            new_version.product = Product.objects.get(slug = self.kwargs['slug'])

            new_version.save()

            return super().form_valid(form)

#initial={'product': Product.objects.get(slug='4')}
