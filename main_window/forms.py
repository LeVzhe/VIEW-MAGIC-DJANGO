from django import forms
from .models import PhotosContent

class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = PhotosContent
        fields = ['user_list', 'description', 'load_img']