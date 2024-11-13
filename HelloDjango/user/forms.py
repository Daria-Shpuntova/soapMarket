from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from soap.models import Zakaz, Dostavka


class UserRegForm(UserCreationForm):
    username = forms.CharField(
        label='Введите логин',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите email'})
    )
 #   some=forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите логин',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    email = forms.EmailField(
        label='Введите email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ZakazForm(forms.ModelForm):
    name = forms.CharField(
        label='Введите ваше имя',
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    email = forms.EmailField(
        label='Введите email',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    phone = forms.CharField(
        label='Введите телефон',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'})
    )
    region = forms.CharField(
        label="Введите регион доставки",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите регион доставки'})
    )
    adress = forms.CharField(
        label='Введите адрес доставки',
        required=True,
        widget = forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите адрес доставки'})
    )
    koment = forms.CharField(
        label='Коментарий к заказу',
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Коментарий к заказу'})
    )
    dostavka = forms.ModelChoiceField(label='Выберите тип доставки',queryset=Dostavka.objects.all())


    class Meta:
        model = Zakaz
        fields = ['name', 'email', 'phone', 'region', 'adress', 'koment', 'dostavka']