from django.contrib import admin
from django.urls import path,include 
from app_sis_vacuna import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_sis_vacuna/', include('app_sis_vacuna.urls')),
    
    #path('listar_todo/',views.listar_todo),
    #path('listar_todo_articulos/',views.listar_todo_articulos),
    #path('ingresar_productos/', views.ingresar_productos),
    #path('ingreso_producto/',views.ingreso_producto),
    
    #path('busqueda_productos/',views.busqueda_productos),
    #path('buscar/',views.buscar),
    #path('eliminar_producto/',views.eliminar_producto),
    #path('eliminacion_producto/',views.eliminacion_producto),
    #path('modificar_articulo/',views.modificar_articulo),
    #path('modificar/',views.modificar),
    
]
