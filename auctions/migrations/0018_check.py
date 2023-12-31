# Generated by Django 4.0.5 on 2022-08-15 13:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_win'),
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=60)),
                ('pn', models.CharField(default='', max_length=60)),
                ('city', models.CharField(default='', max_length=60)),
                ('pinc', models.CharField(default='', max_length=60)),
                ('i', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyitem', to='auctions.listings')),
                ('u', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
