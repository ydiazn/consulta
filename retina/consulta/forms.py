# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django import forms
from models import Paciente, Consulta
from widgets import DatePicker, DateTimePicker, ChosenInput, ChosenInputMultiple
from datetime import datetime


# Yusdanis Feus Pérez
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        exclude = ['numero_historia_clinica']
        widgets = {
            'area_salud': ChosenInput,
            'sexo': ChosenInput,
            'especialidad': ChosenInput,
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
            'especialidad': ChosenInput,
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
        self.fields['fecha'].initial = datetime.now()


class ConsultaPacienteForm(ConsultaForm):

    class Meta(ConsultaForm.Meta):
        exclude = ['paciente']

    def __init__(self, *args, **kwargs):
        self.paciente = kwargs.pop('paciente')
        super(ConsultaPacienteForm, self).__init__(*args, **kwargs)
        if self.paciente_ya_atendido():
            self.fields.pop('caso_nuevo')

    def save(self, commit=True):
        consulta = super(ConsultaPacienteForm, self).save(commit=False)
        consulta.paciente = self.paciente

        if self.paciente_ya_atendido():
            consulta.caso_nuevo = False

        if commit:
            consulta.save()
            self.save_m2m()

        return consulta

    def paciente_ya_atendido(self):
        return self.paciente.consulta_set.all()

