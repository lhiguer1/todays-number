# Generated by Django 4.0.8 on 2023-02-06 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lynchnumbers', '0008_lynchvideo_lynchvideoinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lynchvideoinfo',
            old_name='lynchVideoId',
            new_name='video',
        ),
    ]