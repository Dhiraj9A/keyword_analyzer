from django.urls import path

from .views import (HomeView, AnalyzeSEOView)
urlpatterns = [
    path("",HomeView.as_view(), name="seo-home"),
    path("analyze/",AnalyzeSEOView.as_view(), name="seo-analyze"),
]