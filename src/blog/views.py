from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView


from core.models import Series, Chapters

# Create your views here.

class HomeView(View):
    template_name = 'blog/home.html'

    def get(self, request):
        data = {
            'series': Series.objects.all(),
            'chapters': Chapters.objects.all(),
        }
        return render(request, self.template_name, data)
    
class DirectoryView(View):
    template_name = 'blog/directory.html'

    def get(self, request):
        data = {
            'series': Series.objects.all(),
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
    # template_name = 'video.html'
    template_name = 'blog/chapter.html'
    model = Chapters
    slug_field = 'chapter_slug'
    context_object_name = 'chapter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        # Obtener el capítulo actual
        current_chapter = self.get_object()
        context['current_chapter'] = current_chapter        
        # Obtener la serie asociada al capítulo actual
        series = current_chapter.chapter_title
        # Obtener todos los capítulos asociados a la serie
        chapters = series.chapters_set.all()
        context['chapters'] = chapters
        # Encontrar el índice del capítulo actual en la lista de todos los capítulos
        current_index = list(chapters).index(current_chapter)        
        # Calcular el índice del capítulo siguiente
        if current_index >= 1:
            next_index = current_index - 1
            next_chapter = chapters[next_index]
            context['next_chapter'] = next_chapter
        # Calcular el índice del capítulo anterior        
        if current_index+1 < len(chapters):
            previus_index = current_index + 1
            previus_chapter = chapters[previus_index]
            context['previus_chapter'] = previus_chapter
        return context

