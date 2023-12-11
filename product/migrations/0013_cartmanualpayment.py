# Generated by Django 4.1 on 2023-12-11 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_boxrow__is_deleted_candy__is_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartManualPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('_is_deleted', models.BooleanField(default=False)),
                ('price', models.PositiveBigIntegerField()),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product.cart')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
