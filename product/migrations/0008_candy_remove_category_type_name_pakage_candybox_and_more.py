# Generated by Django 4.1 on 2023-11-17 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_image'),
        ('product', '0007_merge_20231117_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.RemoveField(
            model_name='category',
            name='type_name',
        ),
        migrations.CreateModel(
            name='Pakage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('balloon', models.BooleanField(default=False)),
                ('candle', models.BooleanField(default=False)),
                ('thread', models.BooleanField(default=False)),
                ('dish', models.BooleanField(default=False)),
                ('images', models.ManyToManyField(to='core.image')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='CandyBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('weight', models.PositiveIntegerField(default=2, verbose_name='Weight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_boxes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='BoxRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='box_rows', to='product.candybox')),
                ('candy', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candy_rows', to='product.candy')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
