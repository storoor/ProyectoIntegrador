# Generated by Django 4.1.6 on 2023-03-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0004_encuesta_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='Age',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Category',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Economy',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='encuesta',
            name='Zone',
            field=models.CharField(max_length=250),
        ),
    ]
