# Generated by Django 4.2.4 on 2023-09-13 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_seller_alter_user_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='seller',
        ),
    ]
