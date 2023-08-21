from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from blog.views import BlogCreateView, BlogListVew, BlogUpdateView, BlogDeleteView, BlogDetailView

urlpatterns = [
                  path('', BlogListVew.as_view(), name="blog_list"),
                  path("blog_new/", BlogCreateView.as_view()),
                  path("blog_detail/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
                  path("blog_upd/<slug:slug>/", BlogUpdateView.as_view()),
                  path("blog_del/<slug:slug>/", BlogDeleteView.as_view())

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
