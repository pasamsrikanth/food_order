# Generated by Django 5.0 on 2023-12-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0006_cart_model_hotel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_model',
            name='total_price',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
