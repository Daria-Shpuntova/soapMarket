# Generated by Django 5.0.6 on 2024-06-27 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soap', '0005_zakaz_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='zakaz',
            name='koment',
            field=models.TextField(null=True, verbose_name='Коментарии'),
        ),
    ]
