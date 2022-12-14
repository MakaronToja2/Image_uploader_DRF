# Generated by Django 4.1.3 on 2022-11-26 10:24

import django.core.validators
from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_alter_image_file_alter_image_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='file2',
            field=versatileimagefield.fields.VersatileImageField(blank=True, default=models.ImageField(blank=True, null=True, upload_to='mediafiles', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]), null=True, upload_to='mediafiles', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]
