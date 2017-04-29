from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import date


# Create your views here.
def index(request):
    fecha = date.today()
    return HttpResponseRedirect(
        reverse(
            'consulta:consulta_por_fecha',
            kwargs={'year': fecha.year, 'month': fecha.month, 'day': fecha.day}
        )

    )
