
from django.core.mail import send_mail
from celery import shared_task
# from .models import 
from django.contrib.auth import get_user_model


@shared_task(bind = True)
def send_email_func(self):
    users = get_user_model().objects.all()

    for user in users:
        mail_subject =" Greeting From LeetMorph"
        message=f"Hello {user.get_username}! \n\n Thank you for registering on our platform. We are excited to have you as part of the community "
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=""
            
        )

        
    return "done"
