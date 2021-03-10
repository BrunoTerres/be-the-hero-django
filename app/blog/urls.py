from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    #path('', views.index, name='home'),
    path('', views.PostListView.as_view(), name='home'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
    path('new/', views.post_new, name='post_new'),
]