# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, PageBreak, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from consulta.models import Consulta
from nucleo.models import Medico
from datetime import date, datetime

LIST_STYLE = TableStyle([
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('FONTSIZE', (0,0), (0,0), 11),
    ('GRID', (0,1), (-1,-1), 1, colors.black),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ALIGN', (0,0), (9,0), 'CENTER'),
    ('ALIGN', (0,4), (0,-1), 'CENTER'),
    ('ALIGN', (3,3), (3,-1), 'CENTER'),
    ('ALIGN', (4,4), (4,-1), 'CENTER'),
    ('ALIGN', (7,4), (7,-1), 'CENTER'),
    ('ALIGN', (8,3), (8,-1), 'CENTER'),
    ('ALIGN', (9,3), (9,-1), 'CENTER'),
    ('LEFTPADDING', (0,0), (-1,-1), 1.5),
    ('RIGHTPADDING', (0,0), (-1,-1), 1.5),
    ('SPAN', (0,0), (9,0)),
    ('SPAN', (0,1), (6,1)),
    ('SPAN', (0,2), (4,2)),
    ('SPAN', (5,2), (6,2)),
    ('SPAN', (7,1), (9,1)),
    ('SPAN', (7,2), (9,2)),
]
)

colWidths = [0.23*inch, .48*inch, 1.7*inch, .33*inch, .33*inch, 2.3*inch, 2.7*inch, 0.23*inch, 0.8*inch, 0.5*inch]

class HojaCargoPorMedicoSesion:

    def __init__(self, consultas):
        self.consultas = consultas
        self.stylesheet = getSampleStyleSheet()

    def generate_table(self):
        data = self.get_table_header()
        data.extend(self.get_table_data())
        return Table(data, style=LIST_STYLE, colWidths=colWidths)

    def get_table_header(self):
        year = self.consultas[0].fecha.year
        month = self.consultas[0].fecha.month
        day = self.consultas[0].fecha.day
        if self.consultas[0].fecha.hour <= 12:
            sesion = '8:00 AM - 12:00 AM'
        else:
            sesion = '1:00 PM - 5:00 PM'
        
        str_medico = unicode('Médico', 'utf-8')

        return [
            ['Hoja de Cargo', '', '', '', '', '', '', '', '', ''],
            ['Unidad: %s' % unicode(self.consultas[0].unidad), '', '', '', '', '', '', 'Fecha: %s/%s/%s' % (day, month, year), '', ''],
            ['Consulta: %s' % unicode(self.consultas[0].especialidad), '', '', '', '', unicode('Médico: %s' % self.consultas[0].medico, 'utf-8'), '', 'Hora: %s' % sesion, '', ''],
            ['No.', 'HC', 'Paciente', 'Edad', 'Sexo', unicode('Dirección', 'utf-8'), unicode('Diagnóstico', 'utf-8'), 'CN', 'CAS', 'MNT']
        ]

    def get_table_data(self):
        data = []
        i = 0
        for consulta in self.consultas:
            data_consulta = [
                i + 1,
                consulta.paciente.numero_historia_clinica,
                Paragraph("<para fontSize=8>%s</para>" % consulta.paciente, self.stylesheet['Normal']),
                consulta.paciente.edad,
                consulta.paciente.sexo,
                Paragraph("<para fontSize=8>%s</para>" % unicode(consulta.paciente.direccion), self.stylesheet['Normal']),
                self._queryset_to_paragraph(consulta.diagnostico.all()),
                self._caso_nuevo_string(consulta),
                consulta.conducta.abreviatura,
                self._queryset_to_paragraph(consulta.mnt.all()),
            ]
            data.append(data_consulta)
            i = i + 1
        return data

    def _caso_nuevo_string(self, consulta):
        if consulta.caso_nuevo:
            return "X"
        else:
            return ""

    def _queryset_to_paragraph(self, queryset):
        i = 0
        items = []
        for element in queryset:
            items.append(Paragraph("<para fontSize=8>%s</para>" % unicode(element), self.stylesheet['Normal']))
        return items


class HojaCargoPorMedico:

    def __init__(self, consultas):
        fecha = consultas[0].fecha
        fecha = datetime(fecha.year, fecha.month, fecha.day, 12, 0, 0)
        self.consultas_manana = consultas.filter(fecha__lte=fecha)
        self.consultas_tarde = consultas.filter(fecha__gt=fecha)
        self.content = []
        self.add_hojas()

    def add_hojas(self):
        if self.consultas_manana:
            hoja = HojaCargoPorMedicoSesion(self.consultas_manana)
            self.content.append(hoja.generate_table())
            if self.consultas_tarde:
                self.content.append(PageBreak())
        if self.consultas_tarde:
            hoja = HojaCargoPorMedicoSesion(self.consultas_tarde)
            self.content.append(hoja.generate_table())


class HojaCargo:

    def __init__(self, year, month, day, file="prueba.pdf", pagesize=letter):
        self.doc = SimpleDocTemplate(file, pagesize=(pagesize[1], pagesize[0]))
        self.content = []
        self.generar_hojas_cargo(year, month, day)

    def generar_hojas_cargo(self, year, month, day):
        flag = False
        for medico in Medico.objects.all():
            consultas = medico.consulta_set.filter(fecha__year=year, fecha__month=month, fecha__day=day)
            if consultas:
                if flag:
                    self.content.append(PageBreak())
                hoja = HojaCargoPorMedico(consultas)
                self.content.extend(hoja.content)
                flag = True


    def write(self):
        self.doc.build(self.content)
