# Generated by Django 3.0.4 on 2020-04-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_po_choose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='po',
            name='choose',
            field=models.CharField(choices=[('BestSeller', 'BestSeller'), ('TomTailor', 'TomTailor'), ('TomyHill', 'TomyHill'), ('Espirit', 'Espirit')], max_length=100),
        ),
    ]
