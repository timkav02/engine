# Generated by Django 2.0.5 on 2018-08-29 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20180829_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='video_actors', to='videos.Video'),
        ),
        migrations.AlterField(
            model_name='category',
            name='videos_like',
            field=models.ManyToManyField(blank=True, related_name='video_categories', to='videos.Video'),
        ),
        migrations.AlterField(
            model_name='flipbook',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='video_images', to='videos.Video'),
        ),
    ]
