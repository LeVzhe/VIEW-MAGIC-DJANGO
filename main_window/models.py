from django.db import models
import time, os


class UserList(models.Model):
    user_name = models.CharField(max_length=20, verbose_name='Имя пользователя', unique=True)

    class Meta:
        verbose_name = 'Имя пользователя'
        verbose_name_plural = 'Имена пользователей'

    def __str__(self):
        return self.user_name

def custom_image_name(instance, filename):
    return 'main_window/db_content/{0}/{1}/{2}'.format(instance.user_list.user_name, instance.file_type, filename)


class PhotosContent(models.Model):
    user_list = models.ForeignKey(UserList, on_delete=models.CASCADE)
    load_img = models.ImageField(upload_to=custom_image_name, verbose_name='Фото', blank=False, null=False)
    description = models.TextField(verbose_name='Информация')
    create_time = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    file_type = models.CharField(max_length=3, verbose_name='Тип файла', default='img')
    is_hidden = models.BooleanField(verbose_name='Поле скрыто?', default=False)

    class Meta:
        verbose_name_plural = 'Списки фотографий'
        verbose_name = 'Список загруженных фотографий'
        ordering = ['-create_time']
        
    def __str__(self):
        return self.user_list.user_name
    
    def save(self, *args, **kwargs):
        new_image_name = str(int(time.time()))
        _, file_extension = os.path.splitext(self.load_img.name)
        self.load_img.name = new_image_name + file_extension

        super(PhotosContent, self).save(*args, **kwargs)
