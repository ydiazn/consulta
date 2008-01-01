from django.shortcuts import render
from django.views.generic import DetailView
from consulta.models import Paciente

# Create your views here.

class DetallePacienteView(DetailView):

    model = Paciente
    template_name='consulta/paciente_detail.html'