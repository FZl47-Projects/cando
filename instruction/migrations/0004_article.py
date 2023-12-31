# Generated by Django 4.1 on 2023-10-05 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruction', '0003_instruction_ingredients_instruction_recipe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image')),
            ],
        ),
    ]
