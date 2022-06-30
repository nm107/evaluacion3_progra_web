from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_sis_vacuna.models import Persona

#index
def index(request):
    return render(request,'app_sis_vacuna/index.html')

#ingreso de persona
def ingresar_persona(request):
    return render(request,"app_sis_vacuna/ingresar_persona.html")

def ingreso_persona(request):
    rut=request.GET["txt_rut"]
    nombre=request.GET["txt_nombre"]
    appaterno=request.GET["txt_appaterno"]
    apmaterno=request.GET["txt_apmaterno"]
    edad=request.GET["txt_edad"]
    vacuna=request.GET["txt_vacuna"]
    fecha=request.GET["txt_fecha"]
    if (len(rut)>0 and len(nombre)>0 and len(appaterno)>0 and len(apmaterno)>0
        and len(edad)>0 and len(vacuna)>0 and len(fecha)>0):
        pro=Persona(rut=rut,nombre=nombre,ap_paterno=appaterno, ap_materno=apmaterno,edad=edad,nombre_vacuna=vacuna, fecha=fecha)  
        pro.save()
        mensaje="Persona ingresado..."
    else:
        mensaje="Persona No ingresado o faltan datos..."
    return HttpResponse(mensaje)


#busqueda de persona    
def busqueda_persona(request):
    return render(request,"app_sis_vacuna/buscar_persona.html") 

def buscar_persona(request):
    if request.GET["txt_rut"]:
        persona = request.GET["txt_rut"]
        personas = Persona.objects.filter(nombre__icontains=persona)
        return render(request,"app_sis_vacuna/listar_persona.html",{"personas":personas,"query":persona})
    else:
        mensaje = "Debe ingresar un nombre de producto"
        return HttpResponse(mensaje)



#eliminar persona
def eliminar_persona(request):
    return render(request,"app_sis_vacuna/eliminar_persona.html")

def eliminacion_personas(request):
    if request.GET["txt_rut"]:
        rut_recibido = request.GET["txt_rut"]
        persona = Persona.objects.filter(rut=rut_recibido)
        if persona:
            per=Persona.objects.get(rut=rut_recibido)
            per.delete()
            mensaje = "persona Eliminado..."
        else:
            mensaje = "persona No eliminado...No existe persona con ese rut"
    else:
        mensaje = "Debe ingresar un rut para la eliminación..."
    return HttpResponse(mensaje)


#listar persona
def listar_persona(request):
    datos = Persona.objects.all()  
    return render(request,"app_sis_vacuna/listar_persona.html",{'personas':datos})
    



