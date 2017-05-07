# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import DayArchiveView
from consulta.models import Paciente, Consulta
from consulta.forms import PacienteForm, ConsultaForm
from datetime import date
from helpers import RegistroPacientesWorkbook
from io import BytesIO
from consulta.pdfprint import HojaCargo

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


class EditarConsultaView(UpdateView):

    model = Consulta
    template_name = 'consulta/consulta_editar.html'
    form_class = ConsultaForm

    def get_success_url(self):
        return reverse('consulta:consulta_por_fecha', kwargs={
            'year': self.object.fecha.year,
            'month': self.object.fecha.month,
            'day': self.object.fecha.day,
        })

    def get_context_data(self, **kwargs):
        context = super(EditarConsultaView, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': 'Consulta'
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
                        'conducta',
                        'MNT',
                        'medico',
                        'hora',
                        'nuevo?',
                    ),
                'menu': 'consulta'
            }
        )
        return context


class EliminarConsultaView(DeleteView):

    model = Consulta

    def get_object(self):
        object = super(EliminarConsultaView, self).get_object()
        self.redirect_url = reverse(
                                'consulta:consulta_por_fecha',
                                kwargs={
                                    'year': object.fecha.year,
                                    'month': object.fecha.month,
                                    'day': object.fecha.day
                                }
                            )
        return object

    def get_success_url(self):
        return self.redirect_url

    def get_context_data(self, **kwargs):
        context = super(EliminarConsultaView, self).get_context_data(**kwargs)
        context.update(
            {
                'url_cancelar': self.redirect_url,
                'menu': 'consulta'
            }
        )
        return context


def registro_pacientes(request, year, month, day):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = Hoja de cargo del %s/%s/%s' % (day, month, year)
    
    #consultas = Consulta.objects.filter(fecha__year=year, fecha__month=month, fecha__day=day)
    consultas = Consulta.objects.all()
    buffer = BytesIO()
    hoja_cargo = HojaCargo(consultas, file=buffer)
    hoja_cargo.write()
    
    response.write(buffer.getvalue())
    buffer.close()
    return response
