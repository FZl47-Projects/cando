# Generated by Django 4.1 on 2023-08-25 03:26

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=400, upload_to=core.models.upload_file_src)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
