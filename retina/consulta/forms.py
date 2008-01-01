# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django import forms
from models import Paciente
from widgets import CalendarWidget


# Yusdanis Feus Pérez
class AdicionarPacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = "__all__"
        widgets = {
            'fecha_nacimiento': CalendarWidget
        }
    
    
    def __init__(self, *args, **kwargs):
        super(AdicionarPacienteForm, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.widget.attrs['class'] = 'form-control'