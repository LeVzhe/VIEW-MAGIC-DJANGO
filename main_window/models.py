from django.db import models
from os.path import splitext
from uuid import uuid4
from django.core.files.storage import FileSystemStorage

class UUIDFileStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        _, ext = splitext(name)
        return 'main_window/db_content/img/' + uuid4().hex + ext


class PhotosContent(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='Название')
    load_img = models.ImageField(upload_to='main_window/db_content/img/', verbose_name='Фото', storage=UUIDFileStorage())
    description = models.TextField(verbose_name='Информация')
    create_time = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    is_hidden = models.BooleanField(verbose_name='Поле скрыто', default=False)

    class Meta:
        verbose_name_plural = 'Списки фотографий'
        verbose_name = 'Список загруженных фотографий'
        ordering = ['-create_time']
        
    def __str__(self):
        return self.user_name
