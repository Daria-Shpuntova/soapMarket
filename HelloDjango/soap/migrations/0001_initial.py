# Generated by Django 5.0.6 on 2024-06-15 12:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aroma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50, verbose_name='Слаг')),
                ('name', models.TextField(verbose_name='Аромат')),
            ],
            options={
                'verbose_name': 'Аромат',
                'verbose_name_plural': 'Ароматы',
            },
        ),
        migrations.CreateModel(
            name='CallMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Имя')),
                ('phone', models.CharField(max_length=17, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('slug', models.CharField(max_length=50, verbose_name='Слаг')),
                ('img', models.TextField(null=True, verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Тип продукта',
                'verbose_name_plural': 'Типы продукта',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=50, verbose_name='Слаг')),
                ('name', models.TextField(verbose_name='Название')),
                ('img', models.TextField(null=True, verbose_name='Картинка')),
                ('price', models.IntegerField(null=True, verbose_name='Цена')),
                ('quantity', models.IntegerField(null=True, verbose_name='количество')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('weight', models.IntegerField(null=True, verbose_name='Вес')),
                ('aroma_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='soap.aroma', verbose_name='Аромат продукта')),
                ('type_prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='soap.type', verbose_name='Тип продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='soap.product')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]
