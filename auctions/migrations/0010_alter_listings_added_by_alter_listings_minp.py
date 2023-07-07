# Generated by Django 4.0.5 on 2022-06-25 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_listings_minp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='listings',
            name='minp',
            field=models.IntegerField(),
        ),
    ]
