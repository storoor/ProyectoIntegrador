# Generated by Django 4.1.6 on 2023-04-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0021_rename_foro_index_lugar_urlmapa_delete_choice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='punt',
            field=models.URLField(default=''),
        ),
    ]