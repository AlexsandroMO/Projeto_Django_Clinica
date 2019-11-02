from django.contrib import admin


from django.contrib import admin
from .models import Genero, TipoExame, NomeExame, Cliente, Paciente, Exame


class ListaPaciente(admin.ModelAdmin):
    list_display = ('nome','cpf','genero','aniversario','cep','empresa',
                    'rua','numero','bairro','cidade','estado','foto')


class ListaCliente(admin.ModelAdmin):
    list_display = ('nome_empresa','cnpj','ramo','cep','rua',
                    'numero','bairro','cidade','estado')


class ListaExame(admin.ModelAdmin):
    list_display = ('nome_paciente','tipo_exame',
                    'data_exame','data_exame_devolucao','exames_padrao','lista_exames','obs_exame')

admin.site.register(Genero)
admin.site.register(TipoExame)
admin.site.register(NomeExame)
admin.site.register(Cliente, ListaCliente)
admin.site.register(Paciente, ListaPaciente)
admin.site.register(Exame, ListaExame)
