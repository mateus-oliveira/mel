# Generated by Django 2.2.12 on 2020-06-27 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minha_app', '0007_auto_20200627_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='url_foto',
            field=models.CharField(max_length=50, null=True),
        ),
    ]