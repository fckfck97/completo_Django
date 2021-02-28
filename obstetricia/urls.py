from django.urls import path
from . import views



urlpatterns = [

	path('parto/', views.InicioParto.as_view(), name='inicio_parto'),
    path('nuevo_paciente/', views.Paciente_Create.as_view(), name='nuevo_paciente'),
    path('parto/examen_fisico/', views.Examen_Fisico_Create.as_view(), name='examen_fisico'),
    path('parto/parto_nuevo/',views.Parto_Create.as_view() , name='parto_nuevo'),
    path('parto/orden_medica_parto/',views.Orden_Medica_Parto_Create.as_view(), name='orden_medica_parto'),
    path('parto/nota_parto/',views.Nota_Parto_Create.as_view(), name='nota_parto'),
    path('resultado/',views.Buscar_Paciente.as_view(), name='buscar_paciente'),
    #Cesarea
    path('cesarea/', views.InicioCesarea.as_view(), name='inicio_cesarea'),
    #Legrado
    path('legrado/', views.InicioLegrado.as_view(), name='inicio_legrado'),
    #Histerectomia
    path('histerectomia/', views.InicioHisterectomia.as_view(), name='inicio_histerectomia'),

    ]

