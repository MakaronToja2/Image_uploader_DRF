from rest_framework import generics

from .models import ImageUploader
from .serializers import ImageSerializerBasic, ImageSerializerPremium, ImageSerializerEnterprise

class ImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ImageUploader.objects.all()
    #need to add another group when needed
    def get_serializer_class(self):
        if self.request.user.groups.filter(name='Basic'):
            return ImageSerializerBasic
        elif self.request.user.groups.filter(name='Premium'):
            return ImageSerializerPremium
        elif self.request.user.groups.filter(name='Enterprise'):
            return ImageSerializerEnterprise

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        serializer.save()

image_list_create_view = ImageListCreateAPIView.as_view()

class ImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ImageUploader.objects.all()
    lookup_field = 'pk'
    # need to add another group when needed
    def get_serializer_class(self):
        if self.request.user.groups.filter(name='Basic'):
            return ImageSerializerBasic
        elif self.request.user.groups.filter(name='Premium'):
            return ImageSerializerPremium
        elif self.request.user.groups.filter(name='Enterprise'):
            return ImageSerializerEnterprise

image_detail_view = ImageDetailAPIView.as_view()

# class ImageUpdateAPIView(generics.UpdateAPIView):
#     queryset = ImageUploader.objects.all()
#     serializer_class = ImageSerializer
#
#     def perform_update(self, serializer):
#         instance = serializer.save()
#
# image_update_view = ImageUpdateAPIView.as_view()
#
# class ImageDestroyAPIView(generics.DestroyAPIView):
#     queryset = ImageUploader.objects.all()
#     serializer_class = ImageSerializer
#     lookup_field = 'pk'
#
#     def perform_destroy(self, instance):
#         super().perform_destroy(instance)
#
# image_destroy_view = ImageDestroyAPIView.as_view()
