# Generated by Django 4.1 on 2023-11-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_candy_remove_category_type_name_pakage_candybox_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
