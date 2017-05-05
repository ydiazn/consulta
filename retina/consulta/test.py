# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.test import TestCase
from django.test import Client
from datetime import date
from dateutil.relativedelta import relativedelta
from .models import Paciente
from nucleo.models import AreaSalud



class EdadPacienteTest(TestCase):
    
    def setUp(self):
        self.fecha_hoy = date.today()
        area = AreaSalud(nombre="13 marzo")
        self.paciente =  Paciente(
            nombres="Yenner",
            primer_apellido="Díaz",
            segundo_apellido="Nuñez",
            numero_historia_clinica="850530",
            ci="85053",
            sexo="M",
            fecha_nacimiento=self.fecha_hoy,
            direccion="Calle 31",
            area_salud=area,
            ocupacion="profesor"
        )

    def test_nino_menor_un_anno(self):
        self.paciente.fecha_nacimiento = self.fecha_hoy - relativedelta(days=1)
        self.assertEquals(self.paciente.edad, 0)
        
    def test_fecha_de_cumpleano(self):
        self.paciente.fecha_nacimiento = self.fecha_hoy - relativedelta(years=1)
        self.assertEquals(self.paciente.edad, 1)
        
    def test_fecha_antes_de_cumpleano(self):
        self.paciente.fecha_nacimiento = self.fecha_hoy - relativedelta(months=8)
        self.assertEquals(self.paciente.edad, 0)
        
    def test_fecha_despues_de_cumpleano(self):
        self.paciente.fecha_nacimiento = self.fecha_hoy - relativedelta(years=1, months=5)
        self.assertEquals(self.paciente.edad, 1)
