# Generated by Django 4.1 on 2023-08-27 02:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_image'),
        ('product', '0011_alter_customorderproduct_factor'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactorCakeImage',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_name', models.CharField(max_length=200)),
                ('track_code', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'ordering': ('-id',),
            },
            bases=('core.image', models.Model),
        ),
    ]