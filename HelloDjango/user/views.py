from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import UserRegForm, UserUpdateForm, ZakazForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from soap.models import Basket, Product, Dostavka, Zakaz, ZakazProd
from soap.forms import BasketUpdate
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import random
import string
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.db import transaction
from HelloDjango.settings import DEFAULT_FROM_EMAIL
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import render_to_string



def register(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('profile')
    else:
        form = UserRegForm()
    return render(
        request,
        'user/reg.html',
        {
            'title': 'Страница регестации',
            'form': form
        })

@login_required
def profile(request):
    if request.method == 'POST':
        updateForm = UserUpdateForm(request.POST, instance=request.user)
        if updateForm.is_valid():
            updateForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:

        updateForm = UserUpdateForm(instance=request.user)

    data = {
        'updateForm': updateForm,
        'baskets': Basket.objects.all(),
        'title': 'Профиль пользователя'
    }
    return render(request, 'user/profile.html', data)

class Basket_page(View, FormMixin):
    model = Basket
    template_name = 'user/basket.html'
    context_object_name = 'basket'
    form_class = ZakazForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        if self.request.user.is_authenticated:
            basket_items = Basket.objects.filter(user=self.request.user)
        else:
            basket_items = Basket.objects.filter(session=self.request.session.session_key)
        return render(request, self.template_name, {self.context_object_name: basket_items, 'form': form})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            rand_b=''.join(random.choice(string.ascii_uppercase) for i in range(10))
            self.numberZakaz = rand_b
            self.name = form.cleaned_data.get('name')
            self.phone = form.cleaned_data.get('phone')
            self.region = form.cleaned_data.get('region')
            self.adress = form.cleaned_data.get('adress')
            self.koment = form.cleaned_data.get('koment')
            if self.request.user.is_authenticated:
                self.user = request.user
                user_list = User.objects.get(user=self.user)
                self.email = user_list.email
            else:
                self.user = None
                self.email = form.cleaned_data.get('email')
            self.request.session.save()
            if self.request.user.is_authenticated:
                self.session = None
            else:
                self.session = Session.objects.get(session_key=self.request.session.session_key)

            return self.form_valid(form)
        else:
            return render(request, self.template_name, {'form': form, 'error': 'Форма заполнена некорректно.'})


    def form_valid(self, form):
        print(52)
        self.object = form.save(commit=False)
        self.object.numberZakaz = self.numberZakaz
        self.object.name = self.name
        self.object.user = self.user
        self.object.session = self.session
        self.object.email = self.email
        self.object.phone = self.phone
        self.object.region = self.region
        self.object.adress = self.adress
        self.object.koment = self.koment
        self.object.save()

        # Теперь сохраняем продукты из корзины в ZakazProd
        if self.object.user != None:
            self.basket_items = Basket.objects.filter(user=self.request.user)
        else:
            self.basket_items = Basket.objects.filter(session=self.request.session.session_key)

        for item in self.basket_items:
            ZakazProd.objects.create(
                adress=self.object,
                product=item.product,
                quantity=item.quantity
            )
        self.all_price = 0
        for itemss in self.basket_items:
            product = Product.objects.get(slug=itemss.product.slug)
            quantity_value = product.quantity
            item_sum = itemss.quantity * product.price
            self.all_price += item_sum
            new_quantity_value = quantity_value - itemss.quantity
            product.quantity = new_quantity_value
            product.save()
        try:
            self.subject = f'Заказ № {self.numberZakaz} в интернет - магазине "Ароматный Меланж"'
            self.user_email = [self.email]
            self.all_basket = len(self.basket_items)
            self.html_content = render_to_string('user/send_mail.html',
                                                 {'basket': self.basket_items, 'len': self.all_basket,
                                                  'allPrice': self.all_price})

        except:
            print("Ошибка ")
        try:

            self.send_mail = EmailMessage(
                self.subject,
                self.html_content,
                'shpdarya@yandex.ru',
                self.user_email
            )
            self.send_mail.content_subtype = "html"
            self.send_mail.send()
        except:
            print("Ошибка при отправке письма")

        for self.items in self.basket_items:
            self.items.delete()
        return redirect(self.get_success_url())


    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object = self.get_object()
        context = super(Basket_page, self).get_context_data(**kwargs)
        return context



@csrf_exempt
def update_quantity(request, *args, **kwargs):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        if request.user.is_authenticated:
            basket_item = get_object_or_404(Basket, product_id=product_id, user=request.user)
        else:
            basket_item = get_object_or_404(Basket, product_id=product_id, session=request.session.session_key)
        basket_item.quantity = quantity
        if basket_item.quantity == '0':
            Basket.objects.filter(id=basket_item.id).delete()

        else:
            basket_item.save()
        return JsonResponse({'success': True})
    else:
        print(41)
        return JsonResponse({'success': False})

    return render(request, "user/basket.html")


@csrf_exempt
def delete_prod(request, *args, **kwargs):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if request.user.is_authenticated:
            basket_item = get_object_or_404(Basket, product_id=product_id, user=request.user)
        else:
            basket_item = get_object_or_404(Basket, product_id=product_id, session=request.session.session_key)
        Basket.objects.filter(id=basket_item.id).delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

    return render(request, "user/basket.html")



#@csrf_exempt
#def update_quantity(request, *args, **kwargs):
#    if request.method == 'POST':
#        print(22)
#        product_id = request.POST.get('product_id')
#        quantity = request.POST.get('quantity')
#        if request.user.is_authenticated:
#            basket_item = get_object_or_404(Basket, product_id=product_id, user=request.user)
#            print(basket_item)
#        else:
#            basket_item = get_object_or_404(Basket, product_id=product_id, session=request.session)
#            print(basket_item)
#        basket_item.quantity = quantity
#        basket_item.save()
#        return JsonResponse({'success': True})
#    else:
#        return JsonResponse({'success': False})


#   def get_context_data(self, *, object_list=None, **kwargs):
#       queryset = kwargs.pop('object_list', None)
#       if queryset is None:
#           self.object_list = self.model.objects.all()
#       context = super(Basket_page, self).get_context_data(**kwargs)
#       if self.request.user.is_authenticated:
#           context['basket_items'] = Basket.objects.filter(user=self.request.user)
#       else:
#           context['basket_items'] = Basket.objects.filter(session=self.request.session.session_key)
#       return context

#class Basket_page(ListView):
#    model = Basket
#    template_name = 'user/basket.html'
#    context_object_name = 'basket'
#
##   def post(self, request, *args, **kwargs):
#       print(22)
#       if request.method == 'POST':
#           roduct_id = request.POST.get('product_id')
#           print(product_id)
#           quantity = request.POST.get('quantity')
#           basket_item = get_object_or_404(Basket, product_id=product_id, user=request.user)
#           basket_item.quantity = quantity
#           basket_item.save()
#           return JsonResponse({'success': True})
#       else:
#           return JsonResponse({'success': False})

#    @method_decorator(csrf_exempt)
#    def update_quantity(request):
#        print(33)
#        if request.method == 'POST':
#           product_id = request.POST.get('product_id')
#           print(product_id)
#           quantity = request.POST.get('quantity')
#           basket_item = get_object_or_404(Basket, product_id=product_id, user=request.user)
#           basket_item.quantity = quantity
#           basket_item.save()
#           return JsonResponse({'success': True})
#        else:
#           return JsonResponse({'success': False})
#


#def basket(request):
#
#    data = {
#        'baskets': Basket.objects.all(),
#        'title': 'Корзина'
#    }
#
#    return render(request, 'user/basket.html', data)

