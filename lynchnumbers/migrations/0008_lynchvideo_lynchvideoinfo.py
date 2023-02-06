# Generated by Django 4.0.8 on 2023-02-06 09:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lynchnumbers', '0007_number_yt_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='LynchVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='lynchvideos')),
            ],
        ),
        migrations.CreateModel(
            name='LynchVideoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.CharField(blank=True, max_length=11, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^[\\w\\-]{11}$')])),
                ('publishedAt', models.DateField(blank=True, null=True)),
                ('transcript', models.TextField(blank=True, null=True)),
                ('number', models.PositiveSmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('lynchVideoId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lynchnumbers.lynchvideo')),
            ],
            options={
                'ordering': ['publishedAt'],
                'get_latest_by': 'publishedAt',
            },
        ),
    ]
