# Generated by Django 4.0.5 on 2022-06-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_bid_minp_listings_minp'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='maxp',
            field=models.IntegerField(null=True),
        ),
    ]
