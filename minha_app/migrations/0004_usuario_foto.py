# Generated by Django 2.2.12 on 2020-06-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_app', '0003_auto_20200601_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.CharField(max_length=20, null=True),
        ),
    ]