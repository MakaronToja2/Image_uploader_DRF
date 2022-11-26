from rest_framework import serializers
from .models import ImageUploader
from versatileimagefield.serializers import VersatileImageFieldSerializer
from datetime import timedelta, datetime
import cv2

# If want to add another group add another serializer
# If would like to add more thumbnail_sizes in settings.py VERSATILEIMAGEFIELD_RENDITION_KEY_SETS add name and value
# If can't use all sizes use example as in ImageSerializerBasic
# If binary image with timer wants to be implemeneted in fields we have to add time_left and binary methods
class ImageSerializer(serializers.ModelSerializer):
    file = VersatileImageFieldSerializer(sizes='image_sizes')
    class Meta:
        model = ImageUploader
        fields = [
            'name',
            'file',
            'time_left',
            'binary',
        ]
class ImageSerializerBasic(serializers.ModelSerializer):
    file = VersatileImageFieldSerializer(sizes=[('thumbnail_200','thumbnail__200x200')])
    class Meta:
        model = ImageUploader
        fields = [
            'name',
            'file',
        ]
class ImageSerializerPremium(serializers.ModelSerializer):
    file = VersatileImageFieldSerializer(sizes='image_sizes')
    class Meta:
        model = ImageUploader
        fields = [
            'name',
            'file',
        ]
class ImageSerializerEnterprise(serializers.ModelSerializer):
    file = VersatileImageFieldSerializer(sizes='image_sizes')
    class Meta:
        model = ImageUploader
        fields = [
            'name',
            'file',
            'time_left',
            'binary',

        ]





