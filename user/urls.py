from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView, LoginView

from django.urls import path

from user.apps import UserConfig
from user.views import RegisterView, ProfileView, SendPasswordView

app_name = UserConfig.name

urlpatterns = [
                  path('', RegisterView.as_view(template_name="user/register.html"), name='user'),
                  path('logout/', LogoutView.as_view(), name='logout'),
                  path('login/', LoginView.as_view(template_name="user/login.html"), name='login'),
                  path('profile/', ProfileView.as_view(template_name="user/profile.html"), name='profile'),
                  path('send_password/', SendPasswordView.as_view(template_name="user/send_password.html"),
                       name='send_password'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
