from django.forms import *
from .models import Genre, Series, Language, Type

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

class SeriesForm(ModelForm):

    serie_title=CharField(
        required=True,
        widget=TextInput(
            attrs={
                'placeholder':'Nombre serie',
                'class':'px-2 border-2 border-[#00eeff] rounded-xl bg-black text-white',
            }
        )
    )

    serie_synopsis=CharField(
        required=False,
        widget=Textarea(
            attrs={
                'class':'w-full px-2 border-2 border-[#00eeff] rounded-xl bg-black text-white'
            }
        )
    )

    serie_genre=ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        required=False,
        widget=CheckboxSelectMultiple(
            attrs={
                'class':'form-check-input',
            }
        )
    )

    serie_language:BooleanField(
        # queryset=Language.objects.all(),
        widget=CheckboxInput(
            attrs={
                'placeholder':'Seleccione el idioma',
                'class':'w-full'
            }
        )
    )

    serie_date_of_issue=DateField(
        required=True,
        widget=DateInput(
            attrs={
                'class':'datepicker'
            }
        )
    )

    

    class Meta:
        model=Series
        fields=['serie_title', 'serie_synopsis', 'serie_genre', 'serie_language', 'serie_type', 'serie_date_of_issue', 'serie_status', 'serie_image_file']



class SeriesForm2(ModelForm):
    class Meta:
        model = Series
        fields='__all__'

    # Puedes agregar validaciones o personalizaciones aquí si es necesario
    # Por ejemplo, puedes agregar widgets personalizados o validadores específicos.

    def clean_serie_genre(self):
        # Ejemplo de validación personalizada para el campo 'serie_genre'
        genre_ids = self.cleaned_data['serie_genre']
        # Realiza las validaciones que necesites aquí
        return genre_ids