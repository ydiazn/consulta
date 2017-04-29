# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django import forms
from models import Paciente, Consulta
from widgets import DatePicker, DateTimePicker, ChosenInput, ChosenInputMultiple


# Yusdanis Feus Pérez
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = "__all__"
        widgets = {
            'fecha_nacimiento': DatePicker,
        }

    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.widget.attrs['class'] = 'form-control'


# Yusdanis Feus Pérez
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = "__all__"
        widgets = {
            'fecha': DateTimePicker,
            'paciente': ChosenInput,
            'diagnostico': ChosenInputMultiple,
            'conducta': ChosenInput,
            'mnt': ChosenInputMultiple
        }

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        for field in self.fields.itervalues():
            field.widget.attrs['class'] = 'form-control'
        self.fields['caso_nuevo'].widget.attrs['class'] = ""
