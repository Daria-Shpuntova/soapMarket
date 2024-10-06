from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views import View
from .models import Type, CallMe, Aroma, Skin_type ,Effect ,Ingredients ,Product, Basket, Newsletter
from django.views.generic.edit import FormMixin
from .forms import CallForm, BasketFM, BasketForm2, News
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.sessions.models import Session



class HomePage(ListView, FormMixin):
    model = Type
    template_name = 'soap/index.html'
    context_object_name = 'type'
    form_class = News

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.email = form.cleaned_data.get('email_form')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.email = self.email
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        self.request.session.save()
        self.session = Session.objects.get(session_key=self.request.session.session_key)
        #        print(self.model.objects.get(slug='vanil'), 'vanil')
        if self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.user)
            print(basket, '11')
        else:
            basket = Basket.objects.filter(session=self.session)
            print(len(basket), '12')
            print(basket, 13)
        context = super(HomePage, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница сайта'
        context['bask'] = len(basket)
        context['aroma'] = Aroma.objects.all()
        return context


class AllProd(ListView, FormMixin):
    model = Product
    template_name = 'soap/all.html'
    context_object_name = 'all'
    form_class = BasketForm2

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.quantity = form.cleaned_data.get('quantity')
            self.product = form.cleaned_data.get('product')
            self.user = request.user if self.request.user.is_authenticated else None
            self.request.session.save()
            if self.request.user.is_authenticated:
                self.session = None
            else:
                self.session = Session.objects.get(session_key=self.request.session.session_key)

#            if self.request.user.is_authenticated:
#                basket_item, created = Basket.objects.get_or_create(user=self.request.user, product=self.product)
#            else:
#                basket_item, created = Basket.objects.get_or_create(session=self.request.session, product=self.product)
#
#            if not created:
#                # Если товар уже есть в корзине, увеличиваем количество на 1
#                basket_item.quantity += 1
#                basket_item.save()
#            else:
#                # Если товара еще нет в корзине, создаем новую запись
#                basket_item.quantity = quantity
#                basket_item.save()

            #            if self.request.session == None:
#                self.request.session.save()
#
#                if request.user.is_authenticated:
#                    self.session = self.request.session.session_key
#
#                else:
#                    self.session = Session.objects.get(session_key=self.request.session.session_key)
#            else:
#                if request.user.is_authenticated:
#                    self.session = self.request.session.session_key
#                else:
#                    self.session = Session.objects.get(session_key=self.request.session.session_key)
#
#            self.session = self.request.session.session_key
#            #           self.session = Session.objects.get(session_key=self.request.session.session_key)
#            if self.session == None:
#                print(self.request.session)
#                print(self.request.session.save())
#                print(self.request.session.session_key, 'session_key')
#                print(self.session, 'self.session')

            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Проверяем, есть ли уже товар в корзине пользователя или сессии

        existing_item = Basket.objects.filter(
            product=self.product,
            user=self.user,
            session=self.session
        ).first()
        print(existing_item)
        if existing_item:
            # Если товар уже есть, увеличиваем количество
            existing_item.quantity += self.quantity
            existing_item.save()
        else:
            self.object = form.save(commit=False)
            self.object.user = self.user
            self.object.session = self.session
            self.object.quantity = self.quantity
            self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('all')

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
            print(self.object_list, 'self.object_list')

        context = super(AllProd, self).get_context_data(**kwargs)
        self.request.session.save()
        self.session = Session.objects.get(session_key=self.request.session.session_key)
#        print(self.model.objects.get(slug='vanil'), 'vanil')
        if self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.user)
            print(basket, '11')
        else:
            basket = Basket.objects.filter(session=self.session)
            print(len(basket), '12')
            print(basket, 13)

        context['title'] = 'Мыло ручной работы'
        context['bask'] = len(basket)
        context['aroma'] = Aroma.objects.all()
        context['skin_type'] = Skin_type.objects.all()
        context['effect'] = Effect.objects.all()
        context['ingredient'] = Ingredients.objects.all()
        context['type'] = Type.objects.all()

        return context


class AllProd_aroma(DetailView, FormMixin):
    model = Aroma
    template_name = 'soap/all.html'
    context_object_name = 'all_aroma'
    form_class = BasketForm2

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.quantity = form.cleaned_data.get('quantity')
            self.product = form.cleaned_data.get('product')
            self.user = request.user if self.request.user.is_authenticated else None
            self.request.session.save()
            if self.request.user.is_authenticated:
                self.session = None
            else:
                self.session = Session.objects.get(session_key=self.request.session.session_key)
            #           self.session = Session.objects.get(session_key=self.request.session.session_key)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.user
        self.object.session = self.session
        self.object.quantity = self.quantity
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AllProd_aroma, self).get_context_data(**kwargs)
        num = Aroma.objects.filter(slug=self.kwargs['slug']).first()
        prod_list = Product.objects.filter(aroma_prod=num).order_by('-quantity')
#        paginator = Paginator(prod_list, 16)
#        page_number = self.request.GET.get("page")
#        if page_number == None:
#            page_number = 1
#        try:
#            prod_list = paginator.page(page_number)
#        except PageNotAnInteger:
#            prod_list = paginator.page(1)
#        except EmptyPage:
#            prod_list = paginator.page(paginator.num_pages)
#        context["page_obj"] = prod_list
        context['all'] = prod_list
        context['aroma'] = Aroma.objects.all()
        context['type'] = Type.objects.all()
        context['name_aroma'] = self.kwargs['slug']
#        context['paginator'] = paginator.page_range
 #       print(paginator.page_range)
        return context


class Type_slug(DetailView, ListView, FormMixin):
    model = Type
    template_name = 'soap/type_slug.html'
    context_object_name = 'type_slug'
    form_class = BasketForm2

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.quantity = form.cleaned_data.get('quantity')
            self.product = form.cleaned_data.get('product')
            self.user = request.user if self.request.user.is_authenticated else None
            self.request.session.save()
            if self.request.user.is_authenticated:
                self.session = None
            else:
                self.session = Session.objects.get(session_key=self.request.session.session_key)
            #self.session = self.request.session.session_key
            #           self.session = Session.objects.get(session_key=self.request.session.session_key)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        existing_item = Basket.objects.filter(
            product=self.product,
            user=self.user,
            session=self.session
        ).first()
        print(existing_item)
        if existing_item:
            # Если товар уже есть, увеличиваем количество
            existing_item.quantity += self.quantity
            existing_item.save()
        else:
            self.object = form.save(commit=False)
            self.object.user = self.user
            self.object.session = self.session
            self.object.quantity = self.quantity
            self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        type_num = Type.objects.filter(slug=self.kwargs['slug']).first()
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        print(self.object_list)
        context = super(Type_slug, self).get_context_data(**kwargs)
        prod_list = Product.objects.filter(type_prod=type_num).order_by('-quantity')

        self.request.session.save()
        self.session = Session.objects.get(session_key=self.request.session.session_key)
        #        print(self.model.objects.get(slug='vanil'), 'vanil')
        if self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.user)
            print(basket, '11')
        else:
            basket = Basket.objects.filter(session=self.session)
            print(len(basket), '12')
            print(basket, 13)
        context["page_obj"] = prod_list
        context['bask'] = len(basket)
        context['prod'] = prod_list
        context['aroma'] = Aroma.objects.all()
        context['type'] = Type.objects.all()
        context['skin_type'] = Skin_type.objects.all()
        context['effect'] = Effect.objects.all()
        context['ingredient'] = Ingredients.objects.all()
        context['name'] = type_num
        context['name_type'] = self.kwargs['slug']
        return context


class Type_aroma_slug(DetailView, FormMixin):
    model = Type
    template_name = 'soap/type_slug.html'
    context_object_name = 'type_aroma_slug'
    form_class = BasketForm2

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.quantity = form.cleaned_data.get('quantity')
            self.product = form.cleaned_data.get('product')
            self.user = request.user if self.request.user.is_authenticated else None
            self.request.session.save()
            if self.request.user.is_authenticated:
                self.session = None
            else:
                self.session = Session.objects.get(session_key=self.request.session.session_key)
 #           self.session = self.request.session.session_key
            #           self.session = Session.objects.get(session_key=self.request.session.session_key)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        existing_item = Basket.objects.filter(
            product=self.product,
            user=self.user,
            session=self.session
        ).first()
        print(existing_item)
        if existing_item:
            # Если товар уже есть, увеличиваем количество
            existing_item.quantity += self.quantity
            existing_item.save()
        else:
            self.object = form.save(commit=False)
            self.object.user = self.user
            self.object.session = self.session
            self.object.quantity = self.quantity
            self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Type_aroma_slug, self).get_context_data(**kwargs)
        type_num = Type.objects.filter(slug=self.kwargs['slug']).first()
        amore_type = Aroma.objects.filter(slug=self.kwargs['slug_aroma']).first()
        print(amore_type)
        prod_list = Product.objects.filter(type_prod=type_num).filter(aroma_prod=amore_type).order_by('-quantity')
        paginator = Paginator(prod_list, 16)
        page_number = self.request.GET.get("page")
        if page_number == None:
            page_number = 1
        try:
            prod_list = paginator.page(page_number)
        except PageNotAnInteger:
            prod_list = paginator.page(1)
        except EmptyPage:
            prod_list = paginator.page(paginator.num_pages)
        context["page_obj"] = prod_list
        context['prod'] = prod_list
        context['aroma'] = Aroma.objects.all()
        context['type'] = Type.objects.all()
        context['name_type'] = self.kwargs['slug']
        context['name_aroma'] = self.kwargs['slug_aroma']
        context['paginator'] = paginator.page_range
        print(self.kwargs['slug'])
        print(self.kwargs['slug_aroma'])
        return context


class Prod(DetailView, FormMixin):
    model = Product
    template_name = 'soap/prod.html'
    context_object_name = 'products'
    form_class = BasketFM

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.user = request.user if self.request.user.is_authenticated else None
            self.request.session.save()
            if self.request.user.is_authenticated:
                self.session = None
            else:
                self.session = Session.objects.get(session_key=self.request.session.session_key)
            self.quantity = form.cleaned_data.get('quantity')
            num = Product.objects.filter(slug=self.kwargs['slug']).first()
            self.product = num
            print(self.quantity, 'self.quantity')
            print(self.product, 'self.product')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        existing_item = Basket.objects.filter(
            product=self.product,
            user=self.user,
            session=self.session
        ).first()
        print(existing_item)
        if existing_item:
            # Если товар уже есть, увеличиваем количество
            existing_item.quantity += 1
            existing_item.save()
        else:
            self.object = form.save(commit=False)
            self.object.user = self.user
            self.object.session = self.session
            self.object.quantity = self.quantity
            self.object.product = self.product
            self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        self.object = self.get_object()
        context = super(Prod, self).get_context_data(**kwargs)
        context['name'] = Product.objects.filter(slug=self.kwargs['slug']).first()
        num = Product.objects.filter(slug=self.kwargs['slug']).first()
        self.request.session.save()
        self.session = Session.objects.get(session_key=self.request.session.session_key)
        #        print(self.model.objects.get(slug='vanil'), 'vanil')
        if self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.user)
        else:
            basket = Basket.objects.filter(session=self.session)

        print(num)
        context['bask'] = len(basket)
        return context

class About(ListView):
    model = Basket
    template_name = 'soap/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
#        self.object = self.get_object()
        context = super(About, self).get_context_data(**kwargs)
        self.request.session.save()
        self.session = Session.objects.get(session_key=self.request.session.session_key)
        if self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.user)
        else:
            basket = Basket.objects.filter(session=self.session)
        context['bask'] = len(basket)
        return context


class Dostavka(ListView):
    model = Basket
    template_name = 'soap/dostavka.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        #        self.object = self.get_object()
        context = super(Dostavka, self).get_context_data(**kwargs)
        self.request.session.save()
        self.session = Session.objects.get(session_key=self.request.session.session_key)
        if self.request.user.is_authenticated:
            basket = Basket.objects.filter(user=self.user)
        else:
            basket = Basket.objects.filter(session=self.session)
        context['bask'] = len(basket)
        return context

def dostavka(request):
    return render(request, 'soap/dostavka.html')