# Generated by Django 4.1.3 on 2023-02-23 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.TextField(default='description', max_length=100, verbose_name='Descrition'),
        ),
    ]
