from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from consulta.models import Paciente
from consulta.forms import AdicionarPacienteForm

# Create your views here.

class DetallePacienteView(DetailView):

    model = Paciente
    template_name='consulta/paciente_detail.html'


class AdicionarPacienteView(CreateView):

    model = Paciente
    template_name = 'consulta/paciente_adicionar.html'
    form_class = AdicionarPacienteForm