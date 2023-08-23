# Generated by Django 4.2.4 on 2023-08-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(upload_to='', verbose_name='изображение (превью)')),
                ('publication_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('published', models.BooleanField()),
                ('views_number', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
