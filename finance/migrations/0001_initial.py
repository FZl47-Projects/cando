# Generated by Django 4.1 on 2023-10-16 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gateway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Gateway Title')),
                ('gateway_request_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='Request Url')),
                ('gateway_verify_url', models.CharField(blank=True, max_length=150, null=True, verbose_name='Verify Url')),
                ('gateway_code', models.CharField(max_length=12, verbose_name='Gateway Code')),
                ('is_enable', models.BooleanField(default=True, verbose_name='Is Enable')),
                ('auth_data', models.TextField(blank=True, null=True, verbose_name='Auth Data')),
            ],
            options={
                'verbose_name': 'Gateway',
                'verbose_name_plural': 'Gateways',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_num', models.IntegerField(unique=True, verbose_name='Invoice Number')),
                ('amount', models.PositiveIntegerField(verbose_name='Payment Amount')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Is Paid Status')),
                ('payment_log', models.TextField(blank=True, verbose_name='Logs')),
                ('authority', models.CharField(blank=True, max_length=64, verbose_name='Authority')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='Time')),
                ('gateway', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Payments', to='finance.gateway')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
    ]