# Generated by Django 2.0.5 on 2018-08-30 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('videos', '0005_auto_20180830_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='videos.Video')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos_taggedvideo_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
