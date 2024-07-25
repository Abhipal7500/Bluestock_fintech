# Generated by Django 5.0.6 on 2024-07-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IPOInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('company_logo_path', models.TextField()),
                ('company_name', models.CharField(max_length=255)),
                ('price_band', models.CharField(max_length=255)),
                ('open', models.CharField(max_length=255)),
                ('close', models.CharField(max_length=255)),
                ('issue_size', models.CharField(max_length=255)),
                ('issue_type', models.CharField(max_length=255)),
                ('listing_date', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('ipo_price', models.CharField(max_length=255)),
                ('listing_price', models.CharField(max_length=255)),
                ('listing_gain', models.CharField(max_length=255)),
                ('cmp', models.CharField(max_length=255)),
                ('current_return', models.CharField(max_length=255)),
                ('rhp', models.CharField(max_length=255)),
                ('drhp', models.CharField(max_length=255)),
            ],
        ),
    ]
