# Generated by Django 4.0.1 on 2022-02-20 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_cliente_carro_alter_cliente_estado_civil_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uf',
            name='nome',
            field=models.CharField(default='', max_length=30, unique=True),
            preserve_default=False,
        ),
    ]
