# Generated by Django 2.0.5 on 2018-09-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_auto_20180901_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='channel',
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(db_index=True, max_length=128),
        ),
    ]
