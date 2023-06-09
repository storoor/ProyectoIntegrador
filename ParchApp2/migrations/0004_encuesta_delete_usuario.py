# Generated by Django 4.1.6 on 2023-03-19 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0003_alter_usuario_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Age', models.IntegerField(choices=[(1, 'Si'), (2, 'No')], default=1)),
                ('Zone', models.IntegerField(choices=[(1, 'Envigado'), (2, 'Sabaneta'), (3, 'Poblado'), (4, 'Laureles')], default=1)),
                ('Economy', models.IntegerField(choices=[(1, 'menor a 50.000 pesos colombianos'), (2, 'entre 50.000 y 150.000 pesos colombianos'), (3, 'mayor a 150.000 pesos colombianos')], default=1)),
                ('Category', models.IntegerField(choices=[(1, 'Restaurantes'), (2, 'Discotecas'), (3, 'Miradores')], default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
