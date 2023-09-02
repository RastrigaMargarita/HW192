from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from catalog.views import Index, UsercontactCreateView, ProductDetailView, \
    ProductUpdateView, ProductCreateView, ProductDeleteView

urlpatterns = [
                  path('', Index.as_view(), name='index'),
                  path('contacts/', UsercontactCreateView.as_view()),
                  path('product/<slug:slug>/', ProductDetailView.as_view()),
                  path('product_create/', ProductCreateView.as_view(), name="product_create"),
                  path('product_update/<slug:slug>/', ProductUpdateView.as_view(), name="product_update"),
                  path("blog_del/<slug:slug>/", ProductDeleteView.as_view(), name="product_delete")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
