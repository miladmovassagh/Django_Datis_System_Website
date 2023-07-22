from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class CustomUser(AbstractUser):
    # phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    # other attributes for field: help_text="یک مقدار صحیح وارد نمایید", validators=[MinLengthValidator(11),MaxLengthValidator(11)]
    phone_number_regex = RegexValidator(regex = r"09[0-9]{9}") # {n}: refers to number of duplicates 
    postal_code_regex = RegexValidator(regex = r"\d{10}") # \d = [0-9] or digit
    national_code_regex = RegexValidator(regex = r"\d{10}")
    phone_number = models.CharField("شماره موبایل", validators = [phone_number_regex], max_length = 11, error_messages = {'invalid': "لطفا یک شماره موبایل معتبر وارد نمایید\nمانند 09123456789"}, unique = True)
    age = models.PositiveIntegerField("سن", validators=[MinValueValidator(1),MaxValueValidator(120)],blank=True, null=True)
    national_code = models.CharField("کد ملی", validators = [national_code_regex], max_length = 10, error_messages = {'invalid': "لطفا یک کد ملی معتبر وارد نمایید"}, blank=True, null=True, unique=True)
    # birth_date = models.DateField("تاریخ تولد",blank=True, null=True)
    city = models.CharField("شهر",max_length=50)
    address = models.TextField("آدرس")
    postal_code = models.CharField("کد پستی", validators = [postal_code_regex], max_length = 10, error_messages = {'invalid': "لطفا یک کد پستی معتبر وارد نمایید"})
    
    class Meta:
        ordering = ("date_joined",)
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"