# Generated by Django 2.2.12 on 2020-06-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadeOrganizacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
                ('endereco', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=30)),
            ],
        ),
    ]
