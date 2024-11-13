from django import forms
from .models import CallMe, Basket, Product, Newsletter

class News(forms.ModelForm):
    email_form = forms.EmailField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Newsletter
        fields = ['email_form']

class CallForm(forms.ModelForm):
    name_form = forms.CharField(
        label='Введите имя',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите имя'}))
    tel_form = forms.CharField(
        label='Введите телефон',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'})
    )
    email_form = forms.EmailField(
        label='Введите email',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'})
    )
    text_form = forms.CharField(
        label='Текст сообщения',
        required=False,
        widget=forms.Textarea(attrs={'rows': 3, 'class': 'form-text', 'placeholder': 'Введите сообщение'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = CallMe
        fields = ['name_form', 'tel_form', 'email_form', 'text_form']


class BasketForm2(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all())
    class Meta:
        model = Basket
        fields = ['product', 'quantity']

class BasketFM(forms.ModelForm):
    quantity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-b'}))

    class Meta:
        model = Basket
        fields = ['quantity']

class BasketUpdate(forms.ModelForm):
    quantity = forms.IntegerField(required=False)

    class Meta:
        model = Basket
        fields = ['quantity']

