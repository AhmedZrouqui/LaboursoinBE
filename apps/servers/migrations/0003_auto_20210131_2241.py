# Generated by Django 3.0.5 on 2021-01-31 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20210131_2100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='server',
            old_name='serverName',
            new_name='name',
        ),
    ]