# Generated by Django 4.2.4 on 2023-08-05 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_suppliers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suppliers',
            new_name='Supplier',
        ),
    ]
