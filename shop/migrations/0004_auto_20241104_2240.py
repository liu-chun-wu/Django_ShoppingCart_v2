# Generated by Django 3.2.15 on 2024-11-04 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_tradingrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='gmail',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='tradingrecord',
            name='introduction',
        ),
        migrations.AlterField(
            model_name='tradingrecord',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]