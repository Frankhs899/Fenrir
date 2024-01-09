from django.contrib import admin
from .models import Genre, Language, Type, Series, Chapters

# Register your models here.

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Type)
admin.site.register(Series)
admin.site.register(Chapters)