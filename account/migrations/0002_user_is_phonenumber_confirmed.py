# Generated by Django 4.1 on 2023-10-05 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_phonenumber_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]