from django.conf.urls import include, url
from views import *


urlpatterns = [
    url(
        r'^detalle/paciente/(?P<pk>\w+)/$',
        DetallePacienteView.as_view(),
        name='detalle_paciente'
    )
]