from django.shortcuts import render

from .models import PhotosContent

db_content = PhotosContent.objects.all()

categories = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'Фотографии', 'url_name': 'photos'},
    {'title': 'Видеозаписи', 'url_name': 'videos'},
    {'title': 'Записи', 'url_name': 'notes'},
]

def index(request):
    data = {
        'menu': categories,
        'title': 'Главная страница'
    }
    return render(request, 'main_window/index.html', context=data)

def show_photos(request):
    data = {
        'menu': categories,
        'title': 'Ваши фотографии',
        'content': db_content,
    }
    return render(request, 'main_window/show_photos.html', context=data)

def show_videos(request):
    data = {
        'menu': categories,
        'title': 'Ваши видеозаписи'
    }
    return render(request, 'main_window/show_videos.html', context=data)

def show_notes(request):
    data = {
        'menu': categories,
        'title': 'Ваши пометки'
    }
    return render(request, 'main_window/show_notes.html', context=data)
