from django.urls import path
from ProyectoWeb import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('estadistica', views.Grafica, name="Estadistica"),
    path('mantenimientoData', views.carga_data, name="MantenimientoData"),
    path('plot', views.plot,name = "Plot") 
]