from django.urls import path, include

from . import views

app_name = 'hero'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.image_upload, name='upload'),
    path('ngo/', views.NgoListView.as_view(), name='ngos'),
    path('ngo/<int:pk>/', views.NgoDetailView.as_view(), name='ngo_detail'),
    path('ngo/create/', views.NgoCreate.as_view(), name='ngo-create'),
    path('ngo/<int:pk>/update/', views.NgoUpdate.as_view(), name='ngo-update'),
    path('ngo/<int:pk>/delete/', views.NgoDelete.as_view(), name='ngo-delete'),
]

