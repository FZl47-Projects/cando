# Generated by Django 4.1 on 2023-08-31 07:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0005_alter_customorderproduct_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment',
            new_name='Factor',
        ),
    ]
