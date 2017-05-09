# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import StringIO
import xlsxwriter

## Tareas pendientes de formato
# Establecer el tamño de la hoja y los márgenes
# Utilizar un tamaño de letra más pequeña
# Establecer el ancho de las columnas
# Ajustar el texto según el ancho de la columna
# Centrar las columnas Edad, Sexo y caso nuevo
# Pintar los bordes de la tabla
class RegistroPacientesWorkbook:

    def __init__(self, consultas):
        self.consultas = consultas
        self.output = StringIO.StringIO()
        self.workbook = xlsxwriter.Workbook(self.output)
        self.worksheet = self.workbook.add_worksheet()
        self._write()

    def xlsx_data(self):
        return self.output.getvalue()

    def write_header(self):
        self.worksheet.merge_range('A1:B3', 'MOD. 53 - 12\nMINISTERIO DE SALUD PUBLICA\nHospitales y policlinicos')
        self.worksheet.merge_range('A4:B4', 'Unidad:%s' % self.consultas[0].unidad)
        self.worksheet.merge_range('C1:E4', 'REGISTRO DE PACIENTES\nATENDIDOS')
        self.worksheet.merge_range('F1:F4', 'Medico de asistencia\n%s' % self.consultas[0].medico)
        self.worksheet.merge_range('G1:I1', 'Fecha')
        self.worksheet.merge_range('G2:G3', self.consultas[0].fecha.day)
        self.worksheet.merge_range('H2:H3', self.consultas[0].fecha.month)
        self.worksheet.merge_range('I2:I3', self.consultas[0].fecha.year)
        self.worksheet.write(3, 6, "Dia")
        self.worksheet.write(3, 7, "Mes")
        self.worksheet.write(3, 8, "Anno")
        self.worksheet.merge_range('J1:K4', 'Hoja No')
        self.worksheet.merge_range('A5:K5', '')

    def write_table_header(self, start):
        self.worksheet.write(start, 0, "No.")
        self.worksheet.write(start, 1, "Paciente")
        self.worksheet.write(start, 2, "Edad")
        self.worksheet.write(start, 3, "Sexo")
        self.worksheet.write(start, 4, "Direccion")
        self.worksheet.write(start, 5, "Diagnostico")
        self.worksheet.merge_range('G%s:I%s' % (start + 1, start + 1), 'MNT')
        self.worksheet.write(start, 9, "Nuevo")
        self.worksheet.write(start, 10, "Conducta")

    def write_table_data(self, start):
        for i in range(len(self.consultas)):
            row = i + start
            self.worksheet.write(row, 0, i + 1)
            self.worksheet.write(row, 1, self.consultas[i].paciente.nombre_completo)
            self.worksheet.write(row, 2, self.consultas[i].paciente.edad)
            self.worksheet.write(row, 3, self.consultas[i].paciente.sexo)
            self.worksheet.write(row, 4, self.consultas[i].paciente.direccion)
            diagnostico_str = ""
            for diagnostico in self.consultas[i].diagnostico.all():
                diagnostico_str = ("%s\n%s" %(diagnostico_str, diagnostico.nombre))
            self.worksheet.write(row, 5, diagnostico_str)
            mnt_str = ""
            for mnt in self.consultas[i].mnt.all():
                mnt_str = ("%s\n%s" % (mnt_str, mnt.nombre))
            self.worksheet.merge_range('G%s:I%s' % (row + 1, row + 1), mnt_str)
            if self.consultas[i].caso_nuevo:
                self.worksheet.write(row, 9, "Si")
            else:
                self.worksheet.write(row, 9, "No")
            self.worksheet.write(row, 10, self.consultas[i].conducta.nombre)

    def _write(self):
        self.write_header()
        self.write_table_header(5)
        self.write_table_data(6)
        self.workbook.close()
