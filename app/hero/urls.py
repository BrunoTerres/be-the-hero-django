from django.urls import path, include

from . import views

app_name = 'hero'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.image_upload, name='upload'),
]

