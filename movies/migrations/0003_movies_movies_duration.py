# Generated by Django 4.1.3 on 2023-02-23 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movies_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='movies_duration',
            field=models.IntegerField(default=45, verbose_name='duration'),
        ),
    ]
