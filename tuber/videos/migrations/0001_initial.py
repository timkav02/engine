# Generated by Django 2.0.5 on 2018-08-18 02:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actors', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Flipbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('embedded', models.CharField(max_length=255, validators=[django.core.validators.URLValidator()])),
                ('url', models.CharField(max_length=255, validators=[django.core.validators.URLValidator()])),
                ('rating', models.FloatField(default=0.0)),
                ('channel', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('views', models.IntegerField(default=0)),
                ('thumbnail', models.URLField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.AddField(
            model_name='flipbook',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
        migrations.AddField(
            model_name='category',
            name='videos_like',
            field=models.ManyToManyField(blank=True, related_name='categories_similar', to='videos.Video'),
        ),
        migrations.AddField(
            model_name='actor',
            name='video',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='videos.Video'),
        ),
    ]
