from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','first_name','last_name', 'email', 'phone_number', 'address', 'city', 'is_staff']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ('phone_number','age','national_code','city','address','postal_code')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ('phone_number','age','national_code','city','address','postal_code')}),
    )
     