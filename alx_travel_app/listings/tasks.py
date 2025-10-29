from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(user_email, booking_id):
    subject = 'Booking Confirmation'
    message = f'Thank you for your booking! Your booking ID is {booking_id}.'
    from_email = 'Travel App <your_email@gmail.com>'
    recipient_list = [user_email]
    
    send_mail(subject, message, from_email, recipient_list)
    return f"Email sent to {user_email}"
