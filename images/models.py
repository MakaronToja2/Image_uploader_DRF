from django.db import models
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from versatileimagefield.fields import VersatileImageField
from datetime import timedelta, datetime
import cv2
import os


def get_time():
    return(datetime.now())

# Create your models here.
class ImageUploader(models.Model):
    name = models.TextField(blank=True, null=True, unique=True)
    file = VersatileImageField(
        upload_to='',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['png','jpg'])])
    time_created = models.DateTimeField(default=get_time, null=True, blank=True)
    time_left = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(30),
            MaxValueValidator(30000)
        ])

    @property
    def expiration(self):
        if self.time_left is not None:
            return (self.time_created + timedelta(seconds=self.time_left))
        return self.time_created
    @property
    def binary(self):
        if get_time() >= self.expiration:
            return ('Sorry but your Binary image expired!')
        else:
            file_name = os.path.basename(self.file.name)
            img = cv2.imread(f'/home/makarontoja/CODING/ImageUploader/mediafiles/{file_name}', 2)
            ret, bw_img = cv2.threshold(img, 127, 192, cv2.THRESH_BINARY)
            new_file_loc = (f'http://127.0.0.1:8000/media/sized_images/binary_{file_name}')
            cv2.imwrite(new_file_loc, bw_img)
            cv2.imwrite(f'/home/makarontoja/CODING/ImageUploader/mediafiles/sized_images/binary_{file_name}', bw_img)
            return new_file_loc



