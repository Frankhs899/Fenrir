# Generated by Django 5.0.1 on 2024-01-07 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='serie_status',
            field=models.CharField(choices=[('En emision', 'En emision'), ('Finalizado', 'Finalizado')], default='Broadcast', max_length=20, verbose_name='Estado'),
        ),
    ]
