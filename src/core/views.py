from django.shortcuts import render, redirect
#importacion de vistas genericas de django
from django.views import View
from django.views.generic import ListView, FormView, UpdateView, DeleteView

#Importando Modelos
from django.db import models
from .models import Genre, Series, Language, Type

#importacion de formalarios del archivo forms.py
from .forms import GenreForm, SeriesForm, SeriesForm2

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
    
# vistas de series
class SeriesRegisterView2(View):
    template_name='core/series/series_form2.html'
    success_url=reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        data={
            'series':Series.objects.all(),
            'genres':Genre.objects.all(),
            'idiomas':Language.objects.all(),
            'tipos':Type.objects.all(),
        }
        return render(request, self.template_name, data)
    
    def post(self, request, *args, **kwargs):
        form = SeriesForm(request.POST, request.FILES)

        if form.is_valid():
            series = form.save(commit=False)
            print("Géneros seleccionados:", request.POST.getlist('serie_genre'))
            # Guarda la instancia de Series para obtener un ID
            series.save()
            print("Géneros seleccionados:", request.POST.getlist('serie_genre'))
            # Ahora, puedes agregar las relaciones muchos a muchos
            series.serie_genre.set(request.POST.getlist('serie_genre'))
            print("Géneros seleccionados:", request.POST.getlist('serie_genre'))

            # Guarda la instancia de Series nuevamente después de agregar las relaciones
            series.save()

            return redirect('home')

        data = {
            'genres': Genre.objects.all(),
            'idiomas': Language.objects.all(),
            'tipos': Type.objects.all(),
            'form': form,
        }
        return render(request, self.template_name, data)
    

class SeriesListView(View):

    template_name='core/series/series_list.html'

    def get(self, request, *args, **kwargs):
        data={
            'series':Series.objects.all(),
        }
        return render(request, self.template_name, data)


# class SeriesListView(ListView):

#     model=Series
#     template_name='core/series/series_list.html'

#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)        
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Listado de series'
#         context['create_url'] = reverse_lazy('series_register2')

#         # Obtener la información de los campos del modelo
#         model_fields = self.model._meta.fields
#         # Crear una lista con los verbose_name de los campos
#         header_names = [field.verbose_name.title() for field in model_fields if isinstance(field, models.Field)]

#         # Agregar la lista de nombres al contexto
#         context['header_names'] = header_names
#         # Agregar los objetos del modelo al contexto
#         context['object_list_with_fields'] = [
#             {
#                 'data': {field.name: getattr(serie, field.name) for field in model_fields if isinstance(field, models.Field)},
#                 # 'editar_url': reverse_lazy('genre_update', kwargs={'pk': serie.pk}),
#                 # 'eliminar_url': reverse_lazy('genre_delete', kwargs={'pk': serie.pk}),
#             } 
#             for serie in context['object_list']
#         ]

#         return context




    #vista de referencia sustutuida por SeriesRegisterView2
class SeriesRegisterView(FormView):
    form_class=SeriesForm
    template_name='core/series/series_form.html'
    success_url=reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro de series'
        context['action'] = 'Registrar'
        context['reverse_url'] = reverse_lazy('home')
        return context

    def form_valid(self, form):
        print(self.form_class)
        form.save()
        return super().form_valid(form)

