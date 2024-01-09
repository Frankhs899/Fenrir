from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from core.models import Series, Chapters

# Create your views here.

class HomeView(View):
    template_name = 'blog/home.html'

    def get(self, request):
        data = {
            'series': Series.objects.all()
        }
        return render(request, self.template_name, data)
    

class InfoSerieView(DetailView):
    template_name = 'blog/info_serie.html'
    model = Series
    slug_field = 'serie_slug'
    context_object_name = 'infoserie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        series = self.get_object()
        chapters = series.chapters_set.all()  # Obtiene todos los capítulos asociados a la serie
        context['chapters'] = chapters
        return context

class InfoChapterView(DetailView):
    template_name = 'blog/chapter.html'
    # template_name = 'chapter.html'
    model = Chapters
    slug_field = 'chapter_slug'
    context_object_name = 'chapter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Asegúrate de que el objeto chapter y otros datos necesarios estén en el contexto
        chapter = self.get_object()
        context['chapter'] = chapter
        print(chapter)
        return context