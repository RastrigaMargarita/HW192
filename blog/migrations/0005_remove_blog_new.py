# Generated by Django 4.2.4 on 2023-08-22 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='new',
        ),
    ]
