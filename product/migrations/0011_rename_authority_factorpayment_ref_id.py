# Generated by Django 4.1 on 2023-09-03 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_factor_process_to_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='factorpayment',
            old_name='authority',
            new_name='ref_id',
        ),
    ]
