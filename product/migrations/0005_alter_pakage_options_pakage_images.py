# Generated by Django 4.1 on 2023-10-23 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_image'),
        ('product', '0004_pakage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pakage',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='pakage',
            name='images',
            field=models.ManyToManyField(to='core.image'),
        ),
    ]
