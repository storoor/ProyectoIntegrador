# Generated by Django 4.1.6 on 2023-04-27 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0023_lugar_punt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='punt',
        ),
    ]
