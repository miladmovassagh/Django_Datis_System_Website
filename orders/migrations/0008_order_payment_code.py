# Generated by Django 4.2 on 2023-07-10 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_order_payment_method_order_send_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_code',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='شناسه پرداخت'),
        ),
    ]
