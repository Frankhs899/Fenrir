from django.urls import path
#Vistas relacionadas a generos
from .views import ListGenreView, GenreRegisterView, GenreUpdateView, GenreDeleteView

urlpatterns = [
    #Urls lista o visualizacion de datos modelos
    path('genre/', ListGenreView.as_view(), name= 'genre'),#Lista de generos

    #Urls nuevos registros
    path('genre/register/', GenreRegisterView.as_view(), name='genre_register'),#Registro de generos

    #Urls Modificar registros
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),

    #Urls Borrar registros
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view(), name='genre_delete'),

]