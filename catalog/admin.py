from django.contrib import admin

from blog.models import Blog
from catalog.models import Product, Category, Usercontact, Supplier


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'description', 'slug', 'picture')
    list_filter = ('category', 'title')
    search_fields = ('title', 'description',)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)


@admin.register(Usercontact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'publication_date', 'published', 'views_number',)
