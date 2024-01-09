from django.urls import path
from .views import ListGenreView, GenreRegisterView

urlpatterns = [
    #Urls lista o visualizacion de datos modelos
    path('genre/', ListGenreView.as_view(), name= 'genre'),#Lista de generos

    #Urls nuevos registros
    path('genre/register/', GenreRegisterView.as_view(), name='genre_register'),#Registro de generos

]