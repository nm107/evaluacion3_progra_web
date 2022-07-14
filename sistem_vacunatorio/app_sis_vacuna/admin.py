from django.contrib import admin


from .models import Persona,Vacuna,Vacunacion

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'ap_paterno', 'ap_materno','edad')
    list_per_page = 200
    
class VacunacionAdmin(admin.ModelAdmin):
    list_display = ('persona', 'vacuna', 'dosis', 'fecha')
    list_per_page = 200

    
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Vacuna)
admin.site.register(Vacunacion,VacunacionAdmin)
#nombre de usuario: admin
#password: 1234