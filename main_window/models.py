from django.db import models

class PhotosContent(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='Название')
    load_img = models.ImageField(upload_to='main_window/db_content/img/', verbose_name='Фото')
    description = models.TextField(verbose_name='Информация')
    create_time = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    is_hidden = models.BooleanField(verbose_name='Поле скрыто', default=False)

    class Meta:
        verbose_name_plural = 'Списки фотографий'
        verbose_name = 'Список загруженных фотографий'
        ordering = ['-create_time']
        
    def __str__(self):
        return self.user_name
