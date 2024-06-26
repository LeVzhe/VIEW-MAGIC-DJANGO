from django.contrib import admin
from .models import PhotosContent

class PhotosContentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'description', 'create_time', 'is_hidden')
    list_display_links = ('user_name', 'description')

admin.site.register(PhotosContent, PhotosContentAdmin)