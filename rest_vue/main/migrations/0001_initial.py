# Generated by Django 5.1.2 on 2024-10-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Информационные ресурсы',
                'verbose_name_plural': 'Информационные ресурсы',
                'db_table': 'informatinresource',
                'ordering': ('id',),
            },
        ),
    ]
