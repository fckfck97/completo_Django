from django.urls import path
from . import views



urlpatterns = [

	path('', views.Inicio.as_view(), name='inicio'),
	path('perfil/<int:pk>/', views.Perfil.as_view(), name='perfil'),
    path('nuevo_paciente/', views.Paciente_Create.as_view(), name='nuevo_paciente'),
    path('examen_fisico/', views.Examen_Fisico_Create.as_view(), name='examen_fisico'),
    path('parto_nuevo/',views.Parto_Create.as_view() , name='parto_nuevo'),
    path('orden_medica_parto/',views.Orden_Medica_Parto_Create.as_view(), name='orden_medica_parto'),
    path('nota_parto/',views.Nota_Parto_Create.as_view(), name='nota_parto'),

    ]

