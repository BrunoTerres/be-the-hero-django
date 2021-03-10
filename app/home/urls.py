from django.urls import path

from . import views

app_name = 'hero'
urlpatterns = [
    path('', views.index, name='home'),
    path('bio/', views.BioView.as_view(), name='bio'),
    path('safe/', views.SafeView.as_view(), name='safe'),
    path('fast/', views.FastView.as_view(), name='fast'),
    path('responsive/', views.ResponsiveView.as_view(), name='responsive'),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('job/<int:pk>', views.JobDetailView.as_view(), name='job_detail'),
    #path('tools/', views.ToolListView.as_view(), name='tools'),
    #path('tool/<int:pk>', views.ToolDetailView.as_view(), name='tool_detail'),
    #path('languages/', views.LanguageListView.as_view(), name='languages'),
    #path('language/<int:pk>', views.LanguageDetailView.as_view(), name='language_detail'),
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    #path('upload', views.image_upload, name="upload"),
    path('tools/', views.tools, name='tools'), 
    path('languages/', views.languages, name='languages'),
]   