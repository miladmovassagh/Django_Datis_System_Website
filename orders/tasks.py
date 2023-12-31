from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"order number {order.id}"
    message = f"Dear {order.user.first_name} {order.user.last_name}. your order is ready"
    mail_sent = send_mail(subject,message,"admin@admin.com",[order.user.email])
    return mail_sent