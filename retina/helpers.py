# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
import StringIO
import xlsxwriter


class RegistroPacientesWorkbook:

    def __init__(self, consultas):
        self.consultas = consultas
        self.output = StringIO.StringIO()
        self.workbook = xlsxwriter.Workbook(self.output)
        self.worksheet = self.workbook.add_worksheet()
        self._write()

    def xlsx_data(self):
        return self.output.getvalue()

    def write_header(self, start):
        # worksheet.merge_range('B7:D8', 'Merged Range', merge_format)
        self.worksheet.write(0, 0, "MOD. 53 - 12")

    def write_table_header(self, start):
        self.worksheet.write(start, 0, "No.")
        self.worksheet.write(start, 1, "Paciente")
        self.worksheet.write(start, 2, "Edad")
        self.worksheet.write(start, 3, "Sexo")
        self.worksheet.write(start, 4, "Direccion")
        self.worksheet.write(start, 5, "Diagnostico")
        self.worksheet.write(start, 6, "MNT")
        self.worksheet.write(start, 7, "Nuevo")
        self.worksheet.write(start, 8, "Conducta")

    def write_table_data(self, start):
        for i in range(len(self.consultas)):
            row = i + start
            self.worksheet.write(row, 0, i + 1)
            self.worksheet.write(row, 1, self.consultas[i].paciente.nombre_completo)
            self.worksheet.write(row, 2, self.consultas[i].paciente.edad)
            self.worksheet.write(row, 3, self.consultas[i].paciente.sexo)
            self.worksheet.write(row, 4, self.consultas[i].paciente.direccion)
            for diagnostico in self.consultas[i].diagnostico.all():
                self.worksheet.write(row, 5, "%s|" % diagnostico.nombre)
            for mnt in self.consultas[i].mnt.all():
                self.worksheet.write(row, 6, "%s|" % mnt.nombre)
            if self.consultas[i].caso_nuevo:
                self.worksheet.write(row, 7, "Si")
            else:
                self.worksheet.write(row, 7, "No")
            self.worksheet.write(row, 8, self.consultas[i].conducta.nombre)

    def _write(self):
        self.write_table_header(6)
        self.write_table_data(7)
        self.workbook.close()
