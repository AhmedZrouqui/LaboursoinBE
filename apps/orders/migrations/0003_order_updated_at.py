# Generated by Django 3.0.5 on 2021-01-31 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210130_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
