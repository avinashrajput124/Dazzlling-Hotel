# Generated by Django 4.0.4 on 2022-11-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ello', '0002_youtube_video_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
