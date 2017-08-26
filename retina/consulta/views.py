# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import DayArchiveView
from django.db.models import Q
from consulta.models import Paciente, Consulta
from consulta.forms import PacienteForm, ConsultaForm, BuscarPacienteForm
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
    queryset = Paciente.objects.all()[:5]
    template_name = 'consulta/paciente_listar_div.html'

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
                'menu': 'paciente',
                'criterio_busqueda': self.criterio_busqueda
            }
        )
        return context

    def get(self, request, *args, **kwargs):
        self.criterio_busqueda = request.GET.get('criterio_busqueda', '')
        if(self.criterio_busqueda):
            self.queryset = self.filtrar_pacientes()

        return super(ListarPacienteView, self).get(request, *args, **kwargs)

    def filtrar_pacientes(self):
        filtro = Q()
        criterios = self.criterio_busqueda.split()

        for criterio in criterios:
            filtro = (
                filtro | 
                Q(nombres__icontains=criterio) |
                Q(primer_apellido__icontains=criterio) |
                Q(segundo_apellido__icontains=criterio)
            )

        return Paciente.objects.filter(filtro)


class ListarConsultaPorPacienteView(ListView):
    model = Consulta
    template_name = 'consulta/consulta_por_paciente_div.html'

    def get_queryset(self):
        self.paciente = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        return self.paciente.consulta_set.all()

    def get_context_data(self, **kwargs):
        context = super(ListarConsultaPorPacienteView, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': 'consulta',
                'paciente': self.paciente
            }
        )
        return context


class ModificarConsultaMixin(object):

    def get_success_url(self):
        return reverse('consulta:consulta_por_fecha', kwargs={
            'year': self.object.fecha.year,
            'month': self.object.fecha.month,
            'day': self.object.fecha.day,
        })    

    def get_context_data(self, **kwargs):
        context = super(ModificarConsultaMixin, self).get_context_data(**kwargs)
        context.update(
            {
                'menu': 'consulta'
            }
        )
        return context


class AdicionarConsultaView(ModificarConsultaMixin, CreateView):

    model = Consulta
    template_name = 'consulta/consulta_adicionar.html'
    form_class = ConsultaForm


class EditarConsultaView(ModificarConsultaMixin, UpdateView):

    model = Consulta
    template_name = 'consulta/consulta_editar.html'
    form_class = ConsultaForm


class EditarConsulta2View(UpdateView):

    model = Consulta
    template_name = 'consulta/consulta_editar.html'
    form_class = ConsultaForm
    
    def get_success_url(self):
        return reverse('consulta:listar_consulta_por_paciente', kwargs={'pk': self.object.paciente.pk})  


class ConsultaPorFechaView(DayArchiveView):

    queryset = Consulta.objects.all()
    date_field = "fecha"
    template_name = 'consulta/consulta_por_fecha_div.html'
    month_format = "%m"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context = super(ConsultaPorFechaView, self).get_context_data(**kwargs)
        context.update(
            {
                'campos':
                    (
                        'tipo',                        
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


class EliminarConsultaContextDataMixin(object):
    
    def get_context_data(self, **kwargs):
        context = super(EliminarConsultaContextDataMixin, self).get_context_data(**kwargs)
        context.update(
            {
                'url_cancelar': self.success_url,
                'menu': 'consulta'
            }
        )
        return context


class EliminarConsultaView(EliminarConsultaContextDataMixin, DeleteView):

    model = Consulta

    def get_object(self):
        object = super(EliminarConsultaView, self).get_object()
        self.success_url = reverse(
                                'consulta:consulta_por_fecha',
                                kwargs={
                                    'year': object.fecha.year,
                                    'month': object.fecha.month,
                                    'day': object.fecha.day
                                }
                            )
        return object


class EliminarConsulta2View(EliminarConsultaContextDataMixin, DeleteView):

    model = Consulta

    def get_success_url(self):
        return reverse('consulta:listar_consulta_por_paciente', kwargs={'pk': self.object.paciente.pk})


def registro_pacientes(request, year, month, day):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = Hoja de cargo del %s/%s/%s' % (day, month, year)
    buffer = BytesIO()
    hoja_cargo = HojaCargo(year, month, day, file=buffer)
    hoja_cargo.write()

    response.write(buffer.getvalue())
    buffer.close()
    return response
