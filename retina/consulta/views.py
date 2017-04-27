# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import DayArchiveView
from consulta.models import Paciente, Consulta
from consulta.forms import PacienteForm, ConsultaForm
from datetime import date

# Create your views here.


# Paciente
class DetallePacienteView(DetailView):

    model = Paciente
    template_name = 'consulta/paciente_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetallePacienteView, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': 'paciente'
            }
        )
        return context


class AdicionarPacienteView(CreateView):

    model = Paciente
    template_name = 'consulta/paciente_adicionar.html'
    form_class = PacienteForm
    success_url = reverse_lazy('consulta:listar_paciente')

    def get_context_data(self, **kwargs):
        context = super(AdicionarPacienteView, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': 'paciente'
            }
        )
        return context


class EditarPacienteView(UpdateView):

    model = Paciente
    template_name = 'consulta/paciente_editar.html'
    form_class = PacienteForm
    success_url = reverse_lazy('consulta:listar_paciente')

    def get_context_data(self, **kwargs):
        context = super(EditarPacienteView, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': 'paciente'
            }
        )
        return context


class EliminarPacienteView(DeleteView):

    model = Paciente
    success_url = reverse_lazy('consulta:listar_paciente')

    def get_context_data(self, **kwargs):
        context = super(EliminarPacienteView, self).get_context_data(**kwargs)
        context.update(
            {
                'url_cancelar': reverse('consulta:listar_paciente'),
                'menu': 'paciente'
            }
        )
        return context


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
                    ),
                'menu': 'paciente'
            }
        )
        return context


class AdicionarConsultaView(CreateView):

    model = Consulta
    template_name = 'consulta/consulta_adicionar.html'
    form_class = ConsultaForm
    success_url = reverse_lazy('consulta:listar_paciente')

    def get_context_data(self, **kwargs):
        context = super(AdicionarConsultaView, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': 'consulta'
            }
        )
        return context


class ConsultaPorFechaView(DayArchiveView):

    queryset = Consulta.objects.all()
    date_field = "fecha"
    template_name = 'consulta/consulta_por_fecha.html'
    month_format = "%m"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(ConsultaPorFechaView, self).get_context_data(**kwargs)
        context.update(
            {
                'campos':
                    (
                        'no. HC',
                        'nombre y apellidos',
                        'diagnóstico',
                        'MNT',
                    ),
                'menu': 'consulta'
            }
        )
        return context
