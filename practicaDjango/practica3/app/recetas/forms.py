# forms.py
from django import forms
from django.core.exceptions import ValidationError

from .models import Receta


class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = ('nombre', 'preparación', 'foto',)

    def validate(self, value):
        super().validate(value)

    def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if data[0].islower():
            raise ValidationError("Debe empezar por mayúscula")
        return data

    def clean_preparación(self):
        data = self.cleaned_data['preparación']
        if data[0].islower():
            raise ValidationError("Debe empezar por mayúscula")
        return data
