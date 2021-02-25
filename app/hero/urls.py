from django.urls import path, include
from django.views.generic.base import TemplateView # new

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.image_upload, name='upload'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
]
