# Generated by Django 4.1 on 2023-11-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendormodel',
            name='fulfillment_rate',
            field=models.FloatField(default=0.0),
        ),
    ]
