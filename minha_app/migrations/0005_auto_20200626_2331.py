# Generated by Django 2.2.12 on 2020-06-26 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minha_app', '0004_usuario_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='foto',
            new_name='url_foto',
        ),
    ]
