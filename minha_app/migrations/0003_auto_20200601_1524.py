# Generated by Django 2.2.12 on 2020-06-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_app', '0002_unidadeorganizacional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidadeorganizacional',
            name='cep',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='unidadeorganizacional',
            name='endereco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='unidadeorganizacional',
            name='telefone',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
