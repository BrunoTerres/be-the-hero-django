from django.urls import path 

from . import views

app_name = 'hero'
urlpatterns = [
    path('', views.index, name='index'),

    path('incidents/', views.IncidentListView.as_view(), name='incidents'), 

    path('incident/<int:pk>', views.IncidentDetailView.as_view(), name='incident-detail'),

    path('incident/create', views.IncidentCreateView.as_view(), name='incident-create'),

    path('incident/<int:pk>/update', views.IncidentUpdateView.as_view(), name='incident-update'),

    path('incident/<int:pk>/delete', views.IncidentDeleteView.as_view(), name='incident-delete'),

    path('ngos/', views.NgoListView.as_view(), name='ngos'),

    path('ngo/<int:pk>', views.NgoDetailView.as_view(), name='ngo-detail'),

    path('ngo/create/', views.NgoCreate.as_view(), name='ngo-create'),

    path('ngo/<int:pk>/update', views.NgoUpdate.as_view(), name='ngo-update'),

    path('ngo/<int:pk>/delete', views.NgoDelete.as_view(), name='ngo-delete'),

    path('upload/', views.image_upload, name='upload'),

#    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
#
#    path('borrowedbooks/', views.LoanedBooksListView.as_view(), name='borrowed-books'),
#
#    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

]