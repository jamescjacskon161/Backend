# Generated by Django 4.1.3 on 2023-02-27 09:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movies_movies_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='poster',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='poster'),
        ),
    ]