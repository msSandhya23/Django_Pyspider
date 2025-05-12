from django.dispatch import receiver
from django.db.auth.models import post_save
from django.contrib.auth.models import User
from django.

@receiver(post_save, sender=User)
def send_mail_for_user(sender,instanse,created,**kwargs):
    if created:
        email = instanse.email
        send_mail(
                subject='Welcome to Our Platform!',
                message=plain_message,
                html_message=html_message,
                from_email='sandhyabehera33090@gmail.com',
                recipient_list=[MUFDO.email],
                fail_silently=False
            )