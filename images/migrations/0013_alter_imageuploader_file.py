# Generated by Django 4.1.3 on 2022-11-26 10:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0012_alter_imageuploader_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageuploader',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='mediafiles', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
