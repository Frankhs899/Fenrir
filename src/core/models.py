from django.db import models
from django.utils.text import slugify
from datetime import datetime
import os
import re

# Modelo de género
class Genre(models.Model):
    genre_name = models.CharField(max_length=100, verbose_name='Nombre del género', unique=True)
    genre_description = models.TextField(verbose_name='Descripción del género', blank=True, null=True)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'
        ordering = ['genre_name']

    def __str__(self):
        return self.genre_name
    
#Modelo de idiomas
class Language(models.Model):
    language_name = models.CharField(max_length=100, verbose_name='Idioma', unique=True)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'
        ordering = ['language_name']

    def __str__(self):
        return self.language_name
    
#Modelo de tipos
class Type(models.Model):
    type_name = models.CharField(max_length=100, verbose_name='Tipo', unique=True)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['type_name']

    def __str__(self):
        return self.type_name
    
class Series(models.Model):

    def get_upload_path_img(instance, filename):
        # Eliminar caracteres no permitidos en nombres de archivos y directorios en Windows
        invalid_chars = r'<>:"/\|?*'
        clean_title = re.sub(f'[{re.escape(invalid_chars)}]', '', instance.serie_title)
        # Construir el nombre del archivo de imagen: titulo_serie_portada.extension
        _, extension = os.path.splitext(filename)
        img_filename = f"{clean_title}_portada{extension}"
        # Construir la ruta de la carpeta para las imágenes de esta serie
        return os.path.join('serie_image_file', clean_title, img_filename)

    status_choices = (
        ('En emision', 'En emision'),
        ('Finalizado', 'Finalizado'),
    )

    serie_title = models.CharField(max_length=250, verbose_name='Titulo', unique=True)
    serie_synopsis = models.TextField(verbose_name='sinopsis', blank=True, null=True)
    serie_genre = models.ManyToManyField(Genre, blank=True, verbose_name='Géneros')
    serie_language = models.ForeignKey(Language, verbose_name='Idioma', on_delete = models.CASCADE)
    serie_type = models.ForeignKey(Type, verbose_name='Tipo', on_delete = models.CASCADE)
    serie_date_of_issue = models.DateField(default=datetime.now, verbose_name='Fecha de emisión', blank=True, null=True)
    serie_upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de carga')
    serie_status = models.CharField(max_length=20, choices=status_choices, default='Broadcast', verbose_name='Estado')
    serie_image_file = models.FileField(upload_to=get_upload_path_img, verbose_name='Imagen de portada')

    # Nuevo campo 'slug'
    serie_slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'
        ordering = ['-serie_upload_date']

    def save(self, *args, **kwargs):
        if not self.serie_slug:
            self.serie_slug = slugify(self.serie_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.serie_title
    
# Modelo de Capitulos

# Obtener ruta de carga videos
def get_upload_path_vid(instance, filename):
    # Eliminar caracteres no permitidos en nombres de archivos y directorios en Windows
    invalid_chars = r'<>:"/\|?*'
    clean_title = re.sub(f'[{re.escape(invalid_chars)}]', '', instance.chapter_title.serie_title)
    # Construye el nombre del archivo de video: titulo_serie_numero_capitulo.extension
    _, extension = os.path.splitext(filename)
    video_filename = f"{clean_title}_Capitulo{instance.chapter_number}{extension}"
    # Construye la ruta de la carpeta para los capítulos de esta serie
    return os.path.join('serie_chapter_videos', clean_title, video_filename)


class Chapters(models.Model):

    chapter_title = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name='Titulo')
    chapter_number = models.PositiveBigIntegerField(verbose_name='Numero capitulo')
    chapter_video = models.FileField(upload_to=get_upload_path_vid, verbose_name='Archivo de video')
    chapter_upload_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de carga')

    chapter_slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Capitulo'
        verbose_name_plural = 'Capitulos'
        unique_together = ('chapter_title', 'chapter_number')
        ordering = ['-chapter_upload_date']
    
    def save(self, *args, **kwargs):
        if not self.chapter_slug:
            clean_title = slugify(self.chapter_title.serie_title)
            self.chapter_slug = f"{clean_title}-{self.chapter_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.chapter_title} - {self.chapter_number}"