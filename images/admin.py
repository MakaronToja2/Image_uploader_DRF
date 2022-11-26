from django.contrib import admin

from .models import ImageUploader

# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'file', 'id']
    search_fields = ['name']
admin.site.register(ImageUploader, ImageAdmin)
