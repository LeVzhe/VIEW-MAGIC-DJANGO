from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('photos/', views.show_photos, name='photos'),
    path('videos/', views.show_videos, name='videos'),
    path('notes/', views.show_notes, name='notes'),
]
