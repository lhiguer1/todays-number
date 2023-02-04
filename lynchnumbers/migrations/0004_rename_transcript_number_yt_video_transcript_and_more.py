# Generated by Django 4.0.8 on 2023-02-04 08:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynchnumbers', '0003_alter_number_options_remove_number_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='number',
            old_name='transcript',
            new_name='yt_video_transcript',
        ),
        migrations.AlterField(
            model_name='number',
            name='url',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='[\\w\\-]{11}')]),
        ),
        migrations.RenameField(
            model_name='number',
            old_name='url',
            new_name='yt_video_id',
        ),
    ]
