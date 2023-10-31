import json
import requests
from django.core.mail import send_mail as _send_email_django
from django.conf import settings
from django_q.tasks import async_task


def send_sms(sms_type, phonenumber, **kwargs):
    def handler_welcome():
        pattern_code = '6f3lm0gumxkgvo6'
        values = {
            'user-name': kwargs.get('name')
        }
        return pattern_code, values

    def handler_register_code():
        pattern_code = '5w5hru1e0w05yrc'
        values = {
            'verification-code': kwargs.get('code')
        }
        return pattern_code, values

    def handler_factor_created():
        pattern_code = '4561bzqjdmt4560'
        values = {
            'factor-payment-link': kwargs.get('factor_link')
        }
        return pattern_code, values

    def handler_factor_paid():
        pattern_code = 'f2kkytqxlc7eufy'
        values = {
            'ref-id': kwargs.get('ref_id')
        }
        return pattern_code, values

    def handler_custom_order_estimated():
        pattern_code = 'anez3795ht2jk4w'
        values = {
            'cart-link': kwargs.get('cart_link')
        }
        return pattern_code, values

    def handler_cart_status():
        pattern_code = 'h9w1yvq12mntzpp'
        values = {
            'user-name': kwargs.get('user_name'),
            'track-code': kwargs.get('track_code'),
            'status-text': kwargs.get('status_text'),
        }
        return pattern_code, values

    def handler_custom_order_rejected():
        pattern_code = 'nmp7pk60w4vme9w'
        values = {
            'user-name': kwargs.get('user_name')
        }
        return pattern_code, values

    def handler_confirmation_code():
        pattern_code = '2qdim141kvoh98r'
        values = {
            'code': kwargs.get('code')
        }
        return pattern_code, values

    # admin | superuser
    def handler_new_custom_order_registered():
        pattern_code = 'dc43j7fnpusrtpc'
        values = {}
        return pattern_code, values

    HANDLERS_DICT = {
        'welcome': handler_welcome,
        'register_code': handler_register_code,
        'factor_created': handler_factor_created,
        'factor_paid': handler_factor_paid,
        'custom_order_estimated': handler_custom_order_estimated,
        'cart_status': handler_cart_status,
        'custom_order_rejected': handler_custom_order_rejected,
        'confirmation_code': handler_confirmation_code,
        # admin | superuser
        'new_custom_order_registered': handler_new_custom_order_registered,
    }

    HANDLER = HANDLERS_DICT.get(sms_type, None)
    if not HANDLER:
        return
    pattern_code, values = HANDLER()

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
    try:
        async_task(requests.request,
                   'POST',
                   settings.SMS_CONFIG['API_URL'],
                   headers=headers,
                   data=payload
                   )
    except:
        pass


def send_email(email, content, **kwargs):
    # send email in background
    async_task(_send_email_django,
               settings.EMAIL_SUBJECT,
               content,
               settings.EMAIL_HOST_USER,
               [email]
               )
