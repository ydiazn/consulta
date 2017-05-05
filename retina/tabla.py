from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch

doc = SimpleDocTemplate("prueba.pdf", pagesize=letter, leftmargin=0.5*inch, rightmargin=0.5*inch)
content = []

data=[
    ['Hoja de Cargo', '', '', '', '', '', '', '', '', ''],
    ['Unidad: CMA de HCMC', '', '', '', '', '', '', 'Fecha: 22/04/2017', '', ''],
    ['Consulta: Retina', '', '', '', '', 'Medico: Yanet Diaz', '', 'Hora: 06:00', '', ''],
    ['No.', 'HC', 'Paciente', 'Edad', 'Sexo', 'Direccion', 'Diagnostico', 'CN', 'CAS', 'MNT'],
    [1, '850530', 'Yenner Diaz Nunez', 31, 'M', 'Calle 31 #1A %32 y 36, Rosa la Bayamesa', 'Retinopatia Diabetica No Proliferativa Moderada', 'Si', 'Tto', 'Hidro'],
    [1, '850530', 'Yenner Diaz Nunez', 1, 'M', 'Calle 31 #1A %32 y 36, Rosa la Bayamesa', 'Degeneracion macular asociada a la edad humeda', 'Si', 'Hidro', 'Tto']]

data2=[
    ['Unidad: CMA de Hospital Carlos Manuel de Cespedes', '', '', '', '', '', 'Hoja de Cargo',  'Fecha: 22/04/2017', '', ''],
    ['Consulta: Retina', '', '', '', '', '', 'Medico: Yanet Diaz', 'Hora: 06:00', '', '']]

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

LIST_STYLE2 = TableStyle([
    ('FONTSIZE', (0,0), (-1,-1), 0.05*inch),
    ('LINEABOVE', (0,0), (-1,-1), 1, colors.black),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
    ('SPAN', (0,0), (2,0)),
    ('SPAN', (0,1), (2,1)),
    ('SPAN', (3,0), (6,0)),
    ('SPAN', (3,1), (6,1)),
    ('SPAN', (7,0), (9,0)),
    ('SPAN', (7,1), (9,1)),]
)

h=Table(data2)
h.setStyle(LIST_STYLE2)

t=Table(data)
t.setStyle(LIST_STYLE)

#content.append(h)
content.append(t)
doc.build(content)
