# Generated by Django 4.1 on 2022-11-10 18:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lynchnumbers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='number',
            name='number',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='number',
            name='url',
            field=models.URLField(validators=[django.core.validators.URLValidator]),
        ),
    ]