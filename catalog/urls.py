from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

import user
from catalog.views import Index, UsercontactCreateView, ProductDetailView, \
    ProductUpdateView, ProductCreateView, ProductDeleteView, VersionCreateView, ProductUpdateViewForModerator

urlpatterns = [
                  path('', Index.as_view(), name='index'),
                  path('contacts/', UsercontactCreateView.as_view()),
                  path('product/<slug:slug>/', ProductDetailView.as_view()),
                  path('product_create/', ProductCreateView.as_view(), name="product_create"),
                  path('product_update/<slug:slug>/', ProductUpdateView.as_view(), name="product_update"),
                  path('product_update_moderator/<slug:slug>/', ProductUpdateViewForModerator.as_view(), name="product_update_moderator"),
                  path('blog_del/<slug:slug>/', ProductDeleteView.as_view(), name="product_delete"),
                  path('<slug:slug>/version_create/', VersionCreateView.as_view(), name="version_create"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
