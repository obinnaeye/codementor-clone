# Generated by Django 2.2.6 on 2019-11-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_freelancer_stripe_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
