# Generated by Django 2.1.4 on 2018-12-11 12:54

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to=articles.models.article_image_folder, verbose_name='Картинка статьи'),
        ),
    ]
