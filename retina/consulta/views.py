# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView
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
    success_url = reverse_lazy('consulta:listar_paciente')


class ListarPacienteView(ListView):

    model = Paciente
    template_name = 'consulta/paciente_listar.html'

    def get_context_data(self, **kwargs):
        context = super(ListarPacienteView, self).get_context_data(**kwargs)
        context.update(
            {
                'campos':
                    (
                        'no. HC', 
                        'nombre y apellidos',
                        'edad',
                        'sexo',
                        'área de salud'
                    )
            }
        )
        return context