# Generated by Django 4.1 on 2023-08-26 05:27

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_product_categories_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(max_length=400, upload_to=product.models.upload_src),
        ),
    ]