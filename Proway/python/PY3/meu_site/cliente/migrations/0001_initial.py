# Generated by Django 4.0.1 on 2022-02-06 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'cidade',
            },
        ),
        migrations.CreateModel(
            name='TpPessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'TpPessoa',
            },
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=2, unique=True)),
            ],
            options={
                'db_table': 'UF',
            },
        ),
        migrations.CreateModel(
            name='CPFCNPJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=13)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.tppessoa')),
            ],
            options={
                'db_table': 'CPFCNPJ',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('nasc', models.DateField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cidade')),
                ('cpfcnpj', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cliente.cpfcnpj')),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cliente.uf'),
        ),
    ]