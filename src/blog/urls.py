from django.urls import path
from .views import HomeView, InfoSerieView, InfoChapterView, DirectoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('directorio/', DirectoryView.as_view(), name='directorio'),
    path('<slug:slug>/', InfoSerieView.as_view(), name='info_serie'),
    path('ver/<slug:slug>/', InfoChapterView.as_view(), name='info_chapter'),
]
