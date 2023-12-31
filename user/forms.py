from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from user.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', "telephone", "avatar", "country")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', "telephone", "avatar", "country")


class SendPasswordForm(forms.Form):
    email = forms.EmailField(label="email", max_length=100)

class EnterCodeForm(forms.Form):
    code = forms.CharField(label="Код", max_length=4)