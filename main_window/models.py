from django.db import models

class ContentDb(models.Model):
    name_field = models.CharField(max_length=20, verbose_name='Название')
    path_field = models.CharField(max_length=20, verbose_name='Папка')
    url_field = models.URLField(verbose_name='Адрес')
    image_field = models.ImageField(upload_to='main_window/db_content/img/', verbose_name='Фото')
    file_field = models.FileField(upload_to='main_window/db_content/videos/', verbose_name='Видео')
    description_field = models.TextField(verbose_name='Информация')
    date_time = models.DateTimeField(auto_now=True, verbose_name='Время загрузки')
