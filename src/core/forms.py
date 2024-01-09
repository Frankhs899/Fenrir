from django.forms import *

from .models import Genre

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

        widgets = {
            'genre_name': TextInput(
                attrs={
                    'class':'bg-[#2cd4d9]',
                    'placeholder':'Nombre del género',
                }
            ),
            'genre_description': Textarea(
                attrs={
                    'class':'bg-[#00eeff]',
                    'placeholder':'Descripción del género',
                }
            ),
        }