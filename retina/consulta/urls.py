from django.conf.urls import include, url
from views import *


urlpatterns = [
    url(
        r'^detalle/paciente/(?P<pk>\w+)/$',
        DetallePacienteView.as_view(),
        name='detalle_paciente'
    ),
    url(
        r'^adicionar/paciente/$',
        AdicionarPacienteView.as_view(),
        name='adicionar_paciente'
    ),
    url(
        r'^editar/paciente/(?P<pk>\w+)/$',
        EditarPacienteView.as_view(),
        name='editar_paciente'
    ),
    url(
        r'^eliminar/paciente/(?P<pk>\w+)/$',
        EliminarPacienteView.as_view(),
        name='eliminar_paciente'
    ),
    url(
        r'^listar/paciente/$',
        ListarPacienteView.as_view(),
        name='listar_paciente'
    ),
    url(
        r'^adicionar/consulta/$',
        AdicionarConsultaView.as_view(),
        name='adicionar_consulta'
    ),
    url(
        r'^consulta_por_fecha/$',
        ConsultaPorFechaView.as_view(),
        name='consulta_por_fecha'
    ),
    
]
