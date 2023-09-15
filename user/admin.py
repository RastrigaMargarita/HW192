from django.contrib import admin
from user.models import Countries, User


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar', 'telephone', 'country')
