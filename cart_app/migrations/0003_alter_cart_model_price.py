# Generated by Django 5.0 on 2023-12-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0002_remove_cart_model_quantity_alter_cart_model_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_model',
            name='price',
            field=models.FloatField(),
        ),
    ]
