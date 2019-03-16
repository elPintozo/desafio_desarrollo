from django import forms

from apps.registros.models import ticket


class ticket_form(forms.ModelForm):

    class Meta:
        model = ticket

        exclude = (
            'fecha_creacion',
        )

        fields = (
            'titulo',
            'descripcion',
            'estado',
        )

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}),
            'estado': forms.Select(attrs={'class': 'form-control', 'required': 'required'}),
        }