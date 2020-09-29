from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), label='Kullanıcı Adı', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}), label='Şifre', max_length=100)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ "username", "email", "password", "password2"]
