from django.contrib import admin
from .models import OrderItem , Order

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','created','update','paid','final_cost','send_method','payment_method','payment_code','order_status']
    list_filter = ('paid','created','update','send_method','payment_method','order_status')
    inlines = [OrderItemInline]
    search_fields = ['payment_code',]