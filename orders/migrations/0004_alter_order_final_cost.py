# Generated by Django 4.2 on 2023-05-23 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_final_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='final_cost',
            field=models.PositiveIntegerField(),
        ),
    ]