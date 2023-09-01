import json
import requests
from django.core.mail import send_mail as _send_email_django
from django.conf import settings
from django_q.tasks import async_task


def send_sms(sms_type, phonenumber, **kwargs):
    pattern_code = None
    values = {}

    if sms_type == 'welcome':
        pattern_code = 'lr6jafxick9jwie'
        values = {
            'user-name': kwargs.get('name')
        }
    elif sms_type == 'register_code':
        pattern_code = '5w5hru1e0w05yrc'
        values = {
            'verification-code': kwargs.get('code')
        }
    elif sms_type == 'factor_created':
        pattern_code = 'e4fxpbh5ol0kpju'
        values = {
            'factor-payment-link': kwargs.get('factor_link')
        }
    elif sms_type == 'custom_order_estimated':
        pattern_code = 'jpp8qhmry1kbf4q'
        values = {
            'cart-link': kwargs.get('cart_link')
        }

    phonenumber = str(phonenumber).replace('+', '')
    payload = json.dumps({
        "pattern_code": pattern_code,
        "originator": settings.SMS_CONFIG['ORIGINATOR'],
        "recipient": phonenumber,
        "values": values
    })

    headers = {
        'Authorization': f"AccessKey {settings.SMS_CONFIG['API_KEY']}",
        'Content-Type': 'application/json'
    }
    async_task(requests.request,
               'POST',
               settings.SMS_CONFIG['API_URL'],
               headers=headers,
               data=payload
               )


def send_email(email, content, **kwargs):
    # send email in background
    async_task(_send_email_django,
               settings.EMAIL_SUBJECT,
               content,
               settings.EMAIL_HOST_USER,
               [email]
               )
