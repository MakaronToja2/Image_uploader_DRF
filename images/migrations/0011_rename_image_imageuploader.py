# Generated by Django 4.1.3 on 2022-11-26 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0010_alter_image_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageUploader',
        ),
    ]