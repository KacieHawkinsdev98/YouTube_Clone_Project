# Generated by Django 3.2.6 on 2021-08-18 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YoutubeClone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='video_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
