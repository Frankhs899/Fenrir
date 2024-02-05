from django.urls import path
#Vistas relacionadas a generos
from .views import ListGenreView, GenreRegisterView, GenreUpdateView, GenreDeleteView
#Vistas relacionadas a series
from .views import SeriesRegisterView2, SeriesListView

urlpatterns = [
    #Urls lista o visualizacion de datos modelos
    path('genre/', ListGenreView.as_view(), name= 'genre'),#Lista de generos
    path('series/', SeriesListView.as_view(), name= 'series'),#Lista de series

    #Urls nuevos registros
    path('genre/register/', GenreRegisterView.as_view(), name='genre_register'),#Registro de generos
    # path('series/', SeriesRegisterView.as_view(), name='series_register'),#Registro de 
    path('series/register', SeriesRegisterView2.as_view(), name='series_register2'),#Registro de series

    #Urls Modificar registros
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),

    #Urls Borrar registros
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view(), name='genre_delete'),

]