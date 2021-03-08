from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.PostListView.as_view(), name='blog'),
    path('blog/<int:pk>', views.PostDetailView.as_view(), name='post')
]