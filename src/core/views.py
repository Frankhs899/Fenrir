from django.shortcuts import render
#importacion de vistas genericas de django
from django.views.generic import ListView, FormView, UpdateView, DeleteView

#Importando Modelos
from django.db import models
from .models import Genre

#importacion de formalarios del archivo forms.py
from .forms import GenreForm

#Importando metodos relacionados con redireccion
from django.urls import reverse_lazy

######################### Vistas relacionadas con los generos de las series ##############################################

#VIsta encargada de listar las categorias existentes
class ListGenreView(ListView):
    model = Genre
    template_name = 'core/genre/genre_list.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de géneros'
        context['create_url'] = reverse_lazy('genre_register')

        # Obtener la información de los campos del modelo
        model_fields = self.model._meta.fields
        # Crear una lista con los verbose_name de los campos
        header_names = [field.verbose_name.title() for field in model_fields if isinstance(field, models.Field)]

        # Agregar la lista de nombres al contexto
        context['header_names'] = header_names
        # Agregar los objetos del modelo al contexto
        context['object_list_with_fields'] = [
            {
                'data': {field.name: getattr(genre, field.name) for field in model_fields if isinstance(field, models.Field)},
                'editar_url': reverse_lazy('genre_update', kwargs={'pk': genre.pk}),
                'eliminar_url': reverse_lazy('genre_delete', kwargs={'pk': genre.pk}),
            } 
            for genre in context['object_list']
        ]

        return context
    
#Vista encargada de la creación de nuevos géneros
class GenreRegisterView(FormView):
    form_class = GenreForm
    template_name = 'core/genre/genre_form.html'
    success_url = reverse_lazy('genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de géneros'
        context['action'] = 'Registrar'
        context['reverse_url'] = reverse_lazy('genre')
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
#Vista encargada de la modificacion de genero ya creados
class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'core/genre/genre_update.html'
    success_url = reverse_lazy('genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar generos'
        context['action'] = 'Editar'
        context['reverse_url'] = reverse_lazy('genre')
        return context

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'core/genre/genre_delete.html'
    success_url = reverse_lazy('genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar género'
        context['action'] = 'Eliminar'
        return context