from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('ingresar_persona/', views.ingresar_persona, name='ingresar_persona'),
    path('ingreso_persona/', views.ingreso_persona),
    path('eliminar_persona/', views.eliminar_persona),
    path('eliminacion_personas/', views.eliminacion_personas),
    path('listar_persona/', views.listar_persona),
    path('busqueda_persona/', views.busqueda_persona),
    path('buscar_persona/', views.buscar_persona),






]