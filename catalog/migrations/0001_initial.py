# Generated by Django 4.2.4 on 2023-08-04 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.CharField(max_length=500, verbose_name='описание')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='наименование')),
                ('description', models.CharField(max_length=500, verbose_name='описание')),
                ('picture', models.ImageField(upload_to='', verbose_name='изображение (превью)')),
                ('price', models.IntegerField(verbose_name='цена за покупку')),
                ('creation_date', models.DateTimeField(verbose_name='дата создания')),
                ('last_changing_date', models.DateTimeField(verbose_name='дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
        ),
    ]
