from django import forms
from .models import *


class FormularioCadstro(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'sobrenome', 'telefone', 'email',
                  'data_nascimento', 'descricao', 'categoria']
