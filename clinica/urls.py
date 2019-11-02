
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='url-home'),
    path('', views.listaPacientes, name='url-lista-pacientes'),
    path('lista_view/<int:id>', views.listaView, name='url-lista-view'),
    path('new_paciente/', views.newPaciente, name='url-new-paciente'),
    path('edit_paciente/<int:id>', views.editPaciente, name='url-edit-paciente'),
    path('delete_paciente/<int:id>', views.deletePaciente, name='url-delete-paciente'),

    path('lista_exames', views.listaExames, name='url-lista-exames'),
    path('lista_views_exames/<int:id>', views.listaViewsExames, name='url-lista-views-exames'),
    path('new_exame/', views.newExame, name='url-new-exame'),
    path('edite_exame/<int:id>', views.editExame, name='url-edit-exme'),
    path('delete_exame/<int:id>', views.deleteExame, name='url-delete-exame'),
    path('quadro_exame/', views.quadroExame, name='url-quadro-exame'),
      
]
