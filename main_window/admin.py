from django.contrib import admin
from .models import PhotosContent, UserList

class PhotosContentAdmin(admin.ModelAdmin):
    list_display = ('user_list', 'description', 'create_time', 'is_hidden')
    list_display_links = ('user_list', 'description')

admin.site.register(PhotosContent, PhotosContentAdmin)

class UserListAdmin(admin.ModelAdmin):
    list_display = ('user_name',)
    list_display_links = ('user_name',)
    
admin.site.register(UserList, UserListAdmin)
