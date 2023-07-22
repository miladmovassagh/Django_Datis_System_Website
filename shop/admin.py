from django.contrib import admin
from .models import Category , Product , Picture

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','name','slug','image']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','available','updated']
    list_filter = ['available','created','updated']
    list_editable = ['available']
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['id','images','product']
    list_filter = ['product']    