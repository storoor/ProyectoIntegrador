# Generated by Django 4.1.6 on 2023-04-26 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParchApp2', '0016_alter_lugar_categoria_alter_lugar_descripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('comentarios', models.CharField(max_length=300)),
                ('calificacion', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='lugar',
            name='LvlEconomico',
            field=models.CharField(choices=[('Menor que 50k', 'Menor que 50k'), ('Entre 50k y 150k', 'Entre 50k y 150k'), ('Más de 150k', 'Más de 150k')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='Zona',
            field=models.CharField(choices=[('Envigado', 'Envigado'), ('Itagui', 'Itagui'), ('Comuna 1, Popular', 'Comuna 1, Popular'), ('Comuna 2, Santa cruz', 'Comuna 2, Santa cruz'), ('Comuna 3, Manrique', 'Comuna 3, Manrique'), ('Comuna 4, Aranjuez', 'Comuna 4, Aranjuez'), ('Comuna 5, Castilla', 'Comuna 5, Castilla'), ('Comuna 9, Buenos aires', 'Comuna 9, Buenos aires'), ('Comuna 10 - La Candelaria', 'Comuna 10 - La Candelaria'), ('Comuna 11, Laureles - Estadio', 'Comuna 11, Laureles - Estadio'), ('Comuna 13 - San javier', 'Comuna 13 - San javier'), ('Comuna 14, Poblado', ' Comuna 14, Poblado'), ('Jardin', 'Jardin'), ('Guatapé', 'Guatapé'), ('La estrella', 'La estrella'), ('Sabaneta', 'Sabaneta')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='categoria',
            field=models.CharField(choices=[('Discoteca', 'Discoteca'), ('Restaurante', 'Restaurante'), ('Mirador', 'Mirador'), ('Centro Comercial', 'Centro Comercial'), ('Parche al aire libre', 'Parche al aire libre'), ('Tour', 'Tour'), ('Museo', 'Museo')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='edad',
            field=models.CharField(choices=[('Menor de edad', 'Menor de edad'), ('Mayor de edad', 'Mayor de edad'), ('Todas las edades a partir de los 8 años', 'Todas las edades a partir de los 8 años')], default='', max_length=50),
        ),
    ]
