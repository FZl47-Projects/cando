# Generated by Django 4.1 on 2023-09-03 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_cartstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartstatus',
            name='status',
            field=models.CharField(choices=[('checking', 'در حال بررسی'), ('accepted', 'تایید'), ('send', 'خروج از مرکز سفارش'), ('delivered', 'تحویل به مشتری')], default='checking', max_length=20),
        ),
    ]