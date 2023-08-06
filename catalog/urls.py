from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from catalog.views import index, contacts_post, item

urlpatterns = [
   path('', index),
   path('contacts/', contacts_post),
   path('item/<int:item_id>', item)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
