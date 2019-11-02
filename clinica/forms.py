from django import forms
from .models import Paciente
from .models import Exame


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('nome','cpf', 'genero','aniversario','empresa',
                  'cep','rua','numero','bairro','cidade','estado',
                  'foto')


class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = ('nome_paciente','tipo_exame', 'data_exame','data_exame_devolucao',
                  'exames_padrao','lista_exames','obs_exame')
