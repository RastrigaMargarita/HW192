from django.contrib import admin

from catalog.models import Product, Category, UserContact, Supplier


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'description',)
    list_filter = ('category', 'title')
    search_fields = ('title', 'description',)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('title',)


@admin.register(UserContact)
class UserContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
