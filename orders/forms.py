from django import forms
from .models import Order

class OrderCreateform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['send_method','payment_method']  
    