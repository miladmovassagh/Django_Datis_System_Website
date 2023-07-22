from django.shortcuts import render , redirect
from .forms import OrderCreateform
from .models import OrderItem
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from coupons.forms import CouponApplyForm

# Create your views here.

@login_required
def order_create(request):
    cart = Cart(request)
    coupon_apply_form = CouponApplyForm()
    
    if request.method == 'POST':
        form = OrderCreateform(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.final_cost = cart.get_total_price_after_discount()
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])  
            cart.clear()
            cart.clear_coupon()
            order_created.delay(order.id)
            # return render(request,'orders/order/created.html',{'order':order})
            request.session['order_id'] = order.id
            return redirect(reverse('zarinpal:request'))
    else:
        form = OrderCreateform()
        return render(request,'orders/order/create.html',{"form":form,"cart":cart,"coupon_apply_form":coupon_apply_form})
    