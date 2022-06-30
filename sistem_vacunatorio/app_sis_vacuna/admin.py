from django.contrib import admin


from .models import Persona,Vacuna,Vacunacion

admin.site.register(Persona)
admin.site.register(Vacuna)
admin.site.register(Vacunacion)