from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta: 
        model = Tarea
        fields = ['titulo', 'descripcion', 'important',]
        widgets = {'titulo' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Escribe el título'}),
            'descripcion' : forms.Textarea(attrs={'class': 'form-control','placeholder':'Escribe la descripción'}),
            'important' : forms.CheckboxInput(attrs={'class': 'form-check-input, m-auto'})  
        } #widget para atributo campos fields
        