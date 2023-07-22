# Generated by Django 4.2 on 2023-06-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_address_remove_order_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='', max_length=50, verbose_name='نحوه پرداخت'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='send_method',
            field=models.CharField(default='ارسال با پست', max_length=50, verbose_name='نحوه ارسال'),
            preserve_default=False,
        ),
    ]