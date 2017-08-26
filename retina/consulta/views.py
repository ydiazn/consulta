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
from consulta.forms import PacienteForm, ConsultaForm, ConsultaPacienteForm
from datetime import date
from helpers import RegistroPacientesWorkbook
from io import BytesIO
from consulta.pdfprint import HojaCargo
from mixin import MenuContextDataMixin

# Create your views here.


# Paciente
class DetallePacienteView(MenuContextDataMixin, DetailView):

    model = Paciente
    template_name = 'consulta/paciente_detail.html'
    menu = 'paciente'


class AdicionarPacienteView(MenuContextDataMixin, CreateView):

    model = Paciente
    template_name = 'consulta/paciente_adicionar.html'
    form_class = PacienteForm
    success_url = reverse_lazy('consulta:listar_paciente')
    menu = 'paciente'


class EditarPacienteView(MenuContextDataMixin, UpdateView):

    model = Paciente
    template_name = 'consulta/paciente_editar.html'
    form_class = PacienteForm
    success_url = reverse_lazy('consulta:listar_paciente')
    menu = 'paciente'


class EliminarPacienteView(MenuContextDataMixin, DeleteView):

    model = Paciente
    success_url = reverse_lazy('consulta:listar_paciente')
    menu = 'paciente'

    def get_context_data(self, **kwargs):
        context = super(EliminarPacienteView, self).get_context_data(**kwargs)
        context.update(
            {
                'url_cancelar': reverse('consulta:listar_paciente'),
            }
        )
        return context


class ListarPacienteView(MenuContextDataMixin, ListView):

    model = Paciente
    queryset = Paciente.objects.all()[:5]
    template_name = 'consulta/paciente_listar_div.html'
    menu = 'paciente'

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


class ListarConsultaPorPacienteView(MenuContextDataMixin, ListView):
    model = Consulta
    template_name = 'consulta/consulta_por_paciente_div.html'
    menu = 'consulta'

    def get_queryset(self):
        self.paciente = get_object_or_404(Paciente, pk=self.kwargs['pk'])
        return self.paciente.consulta_set.all()

    def get_context_data(self, **kwargs):
        context = super(ListarConsultaPorPacienteView, self).get_context_data(**kwargs)
        context.update(
            {
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


class AdicionarConsultaView(MenuContextDataMixin, ModificarConsultaMixin, CreateView):

    model = Consulta
    template_name = 'consulta/consulta_adicionar.html'
    form_class = ConsultaForm
    menu = 'consulta'


class AdicionarConsultaPacienteView(MenuContextDataMixin, CreateView):

    model = Consulta
    template_name = 'consulta/consulta_adicionar.html'
    form_class = ConsultaPacienteForm
    success_url = reverse_lazy('consulta:listar_paciente')
    menu = 'paciente'

    def get_form_kwargs(self):
        kwargs = super(AdicionarConsultaPacienteView, self).get_form_kwargs()
        kwargs.update({
            "paciente": get_object_or_404(Paciente, pk=self.kwargs['paciente'])
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super(AdicionarConsultaPacienteView, self).get_context_data(**kwargs)
        paciente = get_object_or_404(Paciente, pk=self.kwargs['paciente'])
        context.update(
            {
                'caso_nuevo': not paciente.consulta_set.all(),
                'paciente': paciente
            }
        )
        return context



class EditarConsultaView(MenuContextDataMixin, ModificarConsultaMixin, UpdateView):

    model = Consulta
    template_name = 'consulta/consulta_editar.html'
    form_class = ConsultaForm
    menu = 'consulta'


class EditarConsulta2View(MenuContextDataMixin, UpdateView):

    model = Consulta
    template_name = 'consulta/consulta_editar.html'
    form_class = ConsultaForm
    menu = 'consulta'
    
    def get_success_url(self):
        return reverse('consulta:listar_consulta_por_paciente', kwargs={'pk': self.object.paciente.pk}) 


class ConsultaPorFechaView(MenuContextDataMixin, DayArchiveView):

    queryset = Consulta.objects.all()
    date_field = "fecha"
    template_name = 'consulta/consulta_por_fecha_div.html'
    month_format = "%m"
    allow_empty = True
    menu = 'consulta'

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
                )
            }
        )
        return context


class EliminarConsultaContextDataMixin(object):
    
    def get_context_data(self, **kwargs):
        context = super(EliminarConsultaContextDataMixin, self).get_context_data(**kwargs)
        context.update(
            {
                'url_cancelar': self.success_url
            }
        )
        return context


class EliminarConsultaView(MenuContextDataMixin, EliminarConsultaContextDataMixin, DeleteView):

    model = Consulta
    menu = "consulta"

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


class EliminarConsulta2View(MenuContextDataMixin, EliminarConsultaContextDataMixin, DeleteView):

    model = Consulta
    menu = "consulta"

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
