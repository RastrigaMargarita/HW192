import random
import string

from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView

from user.forms import RegisterForm, UserProfileForm, SendPasswordForm
from user.models import User


class RegisterView(CreateView):
    """Контроллер для регистрации пользователя"""
    model = User
    form_class = RegisterForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:login')


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return self.request.user


class SendPasswordView(TemplateView):
    template_name = "user/send_password.html"
    form_class = SendPasswordForm
    success_url = reverse_lazy("user:login")

    def post(self, request):
        email_to_send = request.POST.get('email')
        print(request)

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(8))

        send_mail(
            'Новый пароль на вход в Megamarket',
            f'Ваш новый пароль: {password}',
            'RME1C@mail.ru',
            [email_to_send],
            fail_silently=False,
        )

        user_details = User.objects.get(email=email_to_send)
        user_details.set_password(password)
        user_details.save()
        print(user_details.password)

        return render(request, self.template_name)
