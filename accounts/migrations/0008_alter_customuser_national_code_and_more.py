# Generated by Django 4.2 on 2023-06-04 21:42

import django.core.validators
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_national_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='national_code',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='کد ملی'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)], verbose_name='شماره موبایل'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='postal_code',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)], verbose_name='کد پستی'),
        ),
    ]
