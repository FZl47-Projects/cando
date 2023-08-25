import json
import requests
import string
import random
import datetime
from django.utils import timezone
from django.core.mail import send_mail as _send_email_django
from django.conf import settings
from django_q.tasks import async_task
from django.contrib import messages


def send_sms(sms_type, phonenumber, **kwargs):

    def handler(pattern_code, values):
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
        response = requests.request("POST", settings.SMS_CONFIG['API_URL'], headers=headers, data=payload)

    def handle_register_code():
        values = {
            'code': kwargs.get('code')
        }
        handler('5w5hru1e0w05yrc', values)

    SMS_TYPES = {
        'register_code': handle_register_code
    }
    handle_type = SMS_TYPES.get(sms_type)
    if handle_type:
        handle_type()
        return True


def send_email(email, content, **kwargs):
    # send email in background
    async_task(_send_email_django,
               settings.EMAIL_SUBJECT,
               content,
               settings.EMAIL_HOST_USER,
               [email]
               )


def random_str(size=15, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_time(frmt='%Y-%m-%d_%H:%M'):
    t = timezone.now()
    if frmt is not None:
        t = t.strftime(frmt)
    return t


def get_timesince_persian(time):
    time_server = get_time(None)

    diff_time = datetime.datetime(time_server.year, time_server.month, time_server.day, time_server.hour,
                                  time_server.minute) - datetime.datetime(time.year, time.month, time.day, time.hour,
                                                                          time.minute)

    diff_time_sec = diff_time.total_seconds()
    # sec = diff_time_sec % 60
    min = int(diff_time_sec // 60 % 60)
    hour = int(diff_time_sec // 3600)
    day = diff_time.days
    result = ''
    if min > 0:
        result = f'{min} دقیقه پیش'
    else:
        result = f'لحظاتی پیش'

    if hour > 0:
        result = f'{hour} ساعت پیش'

    if day > 0:
        result = f'{day}  روز پیش'

    return result


def add_prefix_phonenum(phonenumber):
    return f'+98{phonenumber}'


def form_validate_err(request, form):
    if form.is_valid() is False:
        errors = form.errors.as_data()
        if errors:
            errors = list(errors.values())
            err = str(errors[0][0])
            err = err.replace('[', '').replace(']', '')
            err = err.replace("'", '')
            messages.error(request, err)
        else:
            messages.error(request, 'دیتای ورودی نامعتبر است')
        return False
    return True