# Generated by Django 4.0.5 on 2022-06-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='image',
        ),
        migrations.AddField(
            model_name='listings',
            name='listimage',
            field=models.ImageField(null=True, upload_to='media/auction/images/'),
        ),
    ]
