from django.shortcuts import render , redirect, get_object_or_404
from orders.models import Order
from django.http import HttpResponse
from zeep import Client
from django.conf import settings

#? sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

client = Client(f'https://{sandbox}.zarinpal.com/pg/services/WebGate/wsdl')
amount = 1000  # Toman / Required
description = "پرداخت هزینه سفارش"  # Required
email = 'ایمیل کاربر'  # Optional
mobile = 'موبایل کاربر'  # Optional
CallbackURL = 'http://localhost:8000/zarinpal/verify/' # Important: need to edit for realy server.

def send_request(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,id=order_id)
    amount = order.final_cost
    email = order.user.email
    result = client.service.PaymentRequest(settings.MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect(f'https://{sandbox}.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request):
    if request.GET.get('Status') == 'OK':
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order,id=order_id)
        result = client.service.PaymentVerification(settings.MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order.paid = True
            order.payment_code = result.RefID
            order.order_status = "در حال آماده سازی"
            order.save()
            # return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
            return render(request,"zarinpal/success.html",{"id":result.RefID})
        elif result.Status == 101:
            # return HttpResponse('Transaction submitted : ' + str(result.Status))
            return render(request,"zarinpal/submitted.html",{"status":result.Status})
        else:
            # return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
            return render(request,"zarinpal/failed.html",{"status":result.Status})
    else:
        # return HttpResponse('Transaction failed or canceled by user')
        return render(request,"zarinpal/cancel.html",{})