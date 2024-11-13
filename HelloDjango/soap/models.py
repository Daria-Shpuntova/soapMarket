from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

class Newsletter(models.Model):
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

class Type(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    slug = models.CharField(max_length=50, verbose_name='Слаг')
    img = models.TextField(null=True, verbose_name='Картинка')

    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продукта'

class CallMe(models.Model):
    name = models.TextField(verbose_name='Имя')
    phone = models.CharField(max_length=17, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Aroma(models.Model):
    slug = models.CharField(max_length=50, verbose_name='Слаг')
    name = models.TextField(verbose_name='Аромат')

    class Meta:
        verbose_name = 'Аромат'
        verbose_name_plural = 'Ароматы'


class Skin_type(models.Model):
    name = models.TextField(verbose_name='Тип кожи')

    class Meta:
        verbose_name = 'Тип кожи'
        verbose_name_plural = 'Типы кожи'

class Effect(models.Model):
    name = models.TextField(verbose_name='Эффект')

    class Meta:
        verbose_name = 'Эффект'
        verbose_name_plural = 'Эффекты'

class Ingredients(models.Model):
    name = models.TextField(verbose_name='Ингредиент')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

class Product(models.Model):
    slug = models.CharField(max_length=50, verbose_name='Слаг')
    name = models.TextField(verbose_name='Название')
    img = models.TextField(null=True, verbose_name='Картинка')
    type_prod = models.ForeignKey('Type', on_delete=models.PROTECT, null=True, verbose_name='Тип продукта')
    aroma_prod = models.ForeignKey('Aroma', on_delete=models.PROTECT, null=True, verbose_name='Аромат продукта')
    skin_type = models.ForeignKey('Skin_type', on_delete=models.PROTECT, null=True, verbose_name='Тип кожи')
    effect = models.ForeignKey('Effect', on_delete=models.PROTECT, null=True, verbose_name='Эффект')
    ingredient = models.ForeignKey('Ingredients', on_delete=models.PROTECT, null=True, verbose_name='Ингредиенты')
    price = models.IntegerField(null=True, verbose_name='Цена')
    quantity = models.IntegerField(null=True, verbose_name='количество')
    description = models.TextField(verbose_name='Описание', null=True)
    weight = models.IntegerField(null=True, verbose_name='Вес')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        if self.user:
            return f'Корзина для {self.user.username} | Продукт {self.product.name}'
        else:
            return f'Корзина для Гостя | Продукт {self.product.name}'

    def summ(self):
        return self.product.price * self.quantity


class Dostavka(models.Model):
    type_d = models.TextField(verbose_name='Вид доставки')
    time_d = models.TextField(null=True, verbose_name='Время доставки')
    price = models.IntegerField(verbose_name='Стоимость доставки')

    class Meta:
        verbose_name = 'Вид доставки'
        verbose_name_plural = 'Виды доставки'

    def __str__(self):
        return self.type_d

class Zakaz(models.Model):
    numberZakaz = models.TextField(verbose_name='Номер заказа')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(verbose_name='Имя')
    email = models.EmailField(verbose_name='E-mail')
    phone = models.CharField(max_length=15, verbose_name='телефон')
    region = models.TextField(null=True, verbose_name="Регион доставки")
    adress = models.TextField(verbose_name="Адрес доставки")
    dostavka = models.ForeignKey(Dostavka, on_delete=models.CASCADE, null=True, blank=True)
    koment = models.TextField(null=True, verbose_name='Коментарии')
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Данные заказа'
        verbose_name_plural = 'Данные заказов'


class ZakazProd(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='количество')
    adress = models.ForeignKey(Zakaz, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Заказанные продукты'
        verbose_name_plural = 'Заказанные продукты'
