from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Имя пользователя',
                               widget = forms.TextInput(attrs={'class':'form-control','placeholder':'Имя пользователя',}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Пароль',}))
    password2 = forms.CharField(label='Подтверждение пароля',
                                widget=forms.PasswordInput(attrs={"class" : "form-control",'placeholder':"Подтверждение пароля"}))
    first_name = forms.CharField(label='Настоящее имя',
                                 widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ваше настоящее имя'}))
    email = forms.EmailField(label='Адресс электронной почты',
                             widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Введите вашу электронную почту'}))
    class Meta():
        model = User
        fields = ('username', 'first_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password1'] != cd['password2']:
                raise forms.ValidationError('Пароли не совпадают')
            return cd['password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя', }))
    password = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', }))