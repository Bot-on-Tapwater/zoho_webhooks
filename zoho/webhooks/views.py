from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .models import EmailWhatsappNotifications, ZohoFormData
import os
from supabase import create_client, Client
from django.conf import settings
import ast
from django.core.mail import send_mail
from django.utils import timezone
from twilio.rest import Client

# Get Supabase credentials from environment variables or settings
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def query_table():
    try:
	    # Query the entire table
        response = supabase.table('zoho_submissions_gc_leads').select('*').execute()

	    # Check if there was an error
        if not response.data:
            print("Error: No data returned.")
            return None

	    # Get the data from the response
        data = response.data
        return data

    except Exception as e:
	    print(f"An error occurred: {e}")
	    return None

def send_notifications(request):
    # Query the data
    data = query_table()
    emailsnotis = EmailWhatsappNotifications.objects.all()
    emails = {notification.email for notification in emailsnotis}

    if data is None:
        return JsonResponse({"error": "Empty table"}, status=404)
    
    for record in data:
        if record['email'] in emails:
            existingRecord = EmailWhatsappNotifications.objects.get(email=record['email'])

            onboardingSubject = 'Generous Circle Onboarding'
            onboardingMessage = 'Use the link provided to proceed to Activation'

            activationSubject = "Generous Circle Activation"
            activationMessage = 'Use the link provided to proceed to Activation'

            notiTime = 300 # Time between sending next notification

            if not existingRecord.onboarding:
                time_since_update = timezone.now() - existingRecord.updated_at

                if time_since_update.total_seconds() >= notiTime: # 5 minutes
                    subject = onboardingSubject
                    message = onboardingMessage

                    send_notification_email(existingRecord.email, subject, message)

                    existingRecord.save(update_fields=['updated_at'])
                
                else:
                    send_notification_email('mundabrandon@outlook.com', 'Notifications', f'Time elapsed since last notification is < {notiTime} seconds')

            if not existingRecord.activation:
                time_since_update = timezone.now() - existingRecord.updated_at

                if time_since_update.total_seconds() >= notiTime: # 5 minutes
                    subject = onboardingSubject
                    message = onboardingMessage

                    send_notification_email(existingRecord.email, subject, message)

                    existingRecord.save(update_fields=['updated_at'])
                
                else:
                    send_notification_email('mundabrandon@outlook.com', 'Notifications', f'Time elapsed since last notification is < {notiTime} seconds')

        else:
            newEntry = EmailWhatsappNotifications.objects.create(email=record['email'], phone=record['phone'])
            newEntry.save()

            send_notification_email(newEntry.email)

            emails.add(record['email'])

    # Pass the data to the template for rendering
    return JsonResponse({"data": str(emails)}, status=200)

def send_notification_email(email, subject=None, message=None):
    if subject is None:
        subject = 'Welcome to Generous Circle'
    
    if message is None:
        message = 'Thank you for registering your account!'

    from_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, from_email, [email])

    send_whatsapp_notification(message)

def send_whatsapp_notification(message):
    client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN'))
    
    message = client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',
        to='whatsapp:+254703676507'
    )

    return message.sid