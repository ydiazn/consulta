from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from consulta.models import Consulta
from datetime import date

LIST_STYLE = TableStyle([
    ('FONTSIZE', (0,1), (-1,-1), 8),
    ('FONTSIZE', (0,0), (0,0), 11),
    ('LINEABOVE', (0,0), (-1,-1), 1, colors.black),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('ALIGN', (0,0), (9,0), 'CENTER'),
    ('ALIGN', (0,3), (0,-1), 'CENTER'),
    ('ALIGN', (3,3), (3,-1), 'CENTER'),
    ('LEFTPADDING', (0,0), (-1,-1), 2),
    ('RIGHTPADDING', (0,0), (-1,-1), 2),
    ('SPAN', (0,0), (9,0)),
    ('SPAN', (0,1), (6,1)),
    ('SPAN', (0,2), (4,2)),
    ('SPAN', (5,2), (6,2)),
    ('SPAN', (7,1), (9,1)),
    ('SPAN', (7,2), (9,2)),
]
)

class HojaCargoPorMedicoSesion:
    
    def __init__(self, consultas):
        self.consultas = consultas
        self.table = Table(self.generate_table())
        self.table.setStyle(LIST_STYLE)
        
    def generate_table(self):
        data = self.get_table_header()
        data.extend(self.get_table_data())
        return data
    
    def get_table_header(self):
        return [
            ['Hoja de Cargo', '', '', '', '', '', '', '', '', ''],
            ['Unidad: %s' % consultas[0].unidad, '', '', '', '', '', '', 'Fecha: %s' % consultas[0].fecha, '', ''],
            ['Consulta: Retina', '', '', '', '', 'Medico: %s' % consultas[0].medico, '', 'Hora: 06:00', '', ''],
            ['No.', 'HC', 'Paciente', 'Edad', 'Sexo', 'Direccion', 'Diagnostico', 'CN', 'CAS', 'MNT']
        ]
    
    def get_table_data(self):
        data = []
        for consulta in self.consultas:
            data_consulta = [
                consulta.paciente.numero_historia_clinica,
                consulta.paciente.ci,
                consulta.paciente,
                consulta.paciente.edad,
                consulta.paciente.sexo,
                consulta.paciente.direccion,
                'Retinopatia Diabetica No Proliferativa Moderada',
                'Si',
                consulta.conducta,
                'Hidro'
            ]
            data.append(data_consulta)
        return data


consultas = Consulta.objects.filter()
doc = SimpleDocTemplate("prueba.pdf", pagesize=letter, leftmargin=0.5*inch, rightmargin=0.5*inch)
content = []
content.append(HojaCargoPorMedicoSesion(consultas).table)
doc.build(content)
