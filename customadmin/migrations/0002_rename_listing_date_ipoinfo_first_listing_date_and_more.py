# Generated by Django 5.0.6 on 2024-08-02 16:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipoinfo',
            old_name='listing_date',
            new_name='first_listing_date',
        ),
        migrations.AddField(
            model_name='ipoinfo',
            name='second_listing_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
