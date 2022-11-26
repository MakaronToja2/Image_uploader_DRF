import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from images.serializers import ImageSerializer, ImageSerializerBasic, ImageSerializerPremium, ImageSerializerEnterprise


from rest_framework.decorators import api_view
from rest_framework.response import Response

from images.models import ImageUploader

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ImageSerializerEnterprise(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        # instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)