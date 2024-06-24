from django.contrib import admin
from django.urls import path, include

from main_window import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_window.urls'))
]
