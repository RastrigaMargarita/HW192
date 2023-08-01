
from django.urls import path

from catalog.views import index, contacts_post

urlpatterns = [
   path('', index),
   path('contacts/', contacts_post)
]
