from django.contrib import admin
from models import Paciente

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombres', 'primer_apellido', 'segundo_apellido', 'foto']


admin.site.register(Paciente, PacienteAdmin)