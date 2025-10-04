from celery import shared_task
from django.core.mail import  send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order_id}'
    message = f'Dear {order.first_name},\n\n' \
        f'You have successfully placed an order.' \
            f'You order ID is {order_id}'
    mail_sent = send_mail(subject,
                          message,
                          'admin@doublewshop.com',
                          [order.email])
    return mail_sent