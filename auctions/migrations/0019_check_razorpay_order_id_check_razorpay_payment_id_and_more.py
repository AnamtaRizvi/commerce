# Generated by Django 4.2.1 on 2023-05-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_check'),
    ]

    operations = [
        migrations.AddField(
            model_name='check',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='check',
            name='razorpay_payment_signature',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]