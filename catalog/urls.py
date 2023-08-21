from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin import forms

from django.urls import path

from catalog.views import Index, UsercontactCreateView, ProductDetailView

urlpatterns = [
                  path('', Index.as_view(), name='index'),
                  path('contacts/', UsercontactCreateView.as_view()),
                  path('product/<slug:slug>/', ProductDetailView.as_view())

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
