# Generated by Django 4.1.3 on 2022-11-26 12:46

import datetime
import django.core.validators
from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0015_alter_imageuploader_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageuploader',
            name='file',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
        migrations.AlterField(
            model_name='imageuploader',
            name='time_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 26, 12, 46, 8, 125745), null=True),
        ),
        migrations.AlterField(
            model_name='imageuploader',
            name='time_left',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(30), django.core.validators.MaxValueValidator(30000)]),
        ),
    ]
