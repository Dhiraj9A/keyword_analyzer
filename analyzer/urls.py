from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze_url, name='analyze_url'),

    path("download-excel/", views.download_excel, name="download_excel"),
    
]