# Generated by Django 3.2.18 on 2023-03-13 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='color',
            new_name='colors',
        ),
    ]
