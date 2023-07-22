from django.db import models
from shop.models import Product
from accounts.models import CustomUser

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomUser, related_name="orders", on_delete=models.CASCADE, verbose_name="کاربر")
    created = models.DateTimeField("تاریخ ایجاد",auto_now_add=True)
    update = models.DateTimeField("تاریخ به روز رسانی",auto_now=True)
    paid = models.BooleanField("وضعیت پرداخت",default=False)
    final_cost = models.PositiveIntegerField("هزینه نهایی")
    send_method = models.CharField("نحوه ارسال", max_length=50)
    payment_method = models.CharField("نحوه پرداخت", max_length=50)
    payment_code = models.PositiveIntegerField("شناسه پرداخت",blank=True,null=True,unique=True)
    order_status = models.CharField("وضعیت سفارش",blank=True,null=True,max_length=30)
    
    class Meta:
        ordering = ('-created',)
        verbose_name = 'سفارش'
        verbose_name_plural = "سفارشات"
    
    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE,verbose_name="سفارش")
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE,verbose_name="محصول")
    price = models.PositiveIntegerField("قیمت")
    quantity = models.PositiveIntegerField("تعداد",default=1)
    
    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
        