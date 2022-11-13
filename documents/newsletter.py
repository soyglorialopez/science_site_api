from django.core.mail import send_mail
from django.conf import settings
from .models import File, Suscription
from datetime import datetime, timedelta

def send_email():
 # send email each sunday
  start_date = datetime.now() - timedelta(days=6)
  end_date = datetime.now()
  recipients = [user.email for user in Suscription.objects.all()]

  # Body for email
  files = File.objects.filter(date__range=(start_date, end_date))
  pub_urls = [f'http://127.0.0.1:8000/files/{file.id}' for file in files]
  pub_urls_to_string =  "\n".join([item for item in pub_urls])
  body = f"Publications of the week \n {pub_urls_to_string}"
  
  # Sending email if there are news publications
  if files:
    send_mail(subject='Newsletter', message=body, from_email=settings.EMAIL_HOST_USER, recipient_list=recipients)

