# Generated by Django 4.1.6 on 2023-04-27 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0025_alter_lugar_punt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lugar',
            name='punt',
            field=models.URLField(default=''),
        ),
    ]
