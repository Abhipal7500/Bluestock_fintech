# Generated by Django 5.0.6 on 2024-07-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_unverifieduser_remove_user_verification_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unverifieduser',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='Email'),
        ),
    ]
