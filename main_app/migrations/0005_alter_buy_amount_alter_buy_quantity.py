# Generated by Django 5.0.4 on 2024-05-22 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_buynow_payment_buynow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='amount',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='buy',
            name='quantity',
            field=models.CharField(max_length=20),
        ),
    ]
