from django.db import models


class EstadosBrasileiros():
    def __init__(self, estado_brasileiro):
        self.estado_brasileiro = estado_brasileiro


EstadosBrasileiros.estado_brasileiro = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('AM', 'Amazonas'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranhão'),
    ('MT', 'Mato Grosso'),
    ('MS', 'Mato Grosso do Sul'),
    ('MG', 'Minas Gerais'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PR', 'Paraná'),
    ('PE', 'Pernambuco'),
    ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'),
    ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('SC', 'Santa Catarina'),
    ('SP', 'São Paulo'),
    ('SE', 'Sergipe'),
    ('TO', 'Tocantins'),
)

class Genero(models.Model):
    tipo = models.CharField(max_length=12, null=False)

    def __str__(self):
        return self.tipo


class TipoExame(models.Model):
    nome_tipo = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nome_tipo


class NomeExame(models.Model):
    nome_exame = models.CharField(max_length=50, null=False)
    valor_exame = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.nome_exame


class Cliente(models.Model):
    ESTADO = EstadosBrasileiros.estado_brasileiro
    nome_empresa = nome_empresa = models.CharField(max_length=70, null=False)
    cnpj = models.CharField(max_length=14, null=False)
    ramo = models.CharField(max_length=50, null=False)
    cep = models.CharField(max_length=8, null=False)
    rua = models.CharField(max_length=100, null=False)
    numero = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    bairro = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    estado = models.CharField(max_length=60, choices=ESTADO, null=False)

    def __str__(self):
        return str(self.nome_empresa) #+ ' - ' + str(self.cnpj)


class Paciente(models.Model):
    ESTADO = EstadosBrasileiros.estado_brasileiro

    nome = models.CharField(verbose_name='NOME',max_length=70, null=False)
    cpf = models.CharField(verbose_name='CPF', max_length=11, null=False)
    genero = models.ForeignKey(Genero, verbose_name='GÊNERO', on_delete=models.CASCADE)
    aniversario = models.DateField(verbose_name='ANIVERSÁRIO', auto_now=False, auto_now_add=False)
    empresa = models.ForeignKey(Cliente, verbose_name='EMPRESA', on_delete=models.CASCADE)
    cep = models.CharField(verbose_name='CEP', max_length=8, null=False)
    rua = models.CharField(verbose_name='RUA', max_length=100, null=False)
    numero = models.DecimalField(verbose_name='NÚMERO', max_digits=6, decimal_places=0, default=0)
    bairro = models.CharField(verbose_name='BAIRRO', max_length=100, null=False)
    cidade = models.CharField(verbose_name='CIDADE', max_length=100, null=False)
    estado = models.CharField(verbose_name='ESTADO', max_length=60, choices=ESTADO, null=False)
    foto = models.ImageField(verbose_name='FOTO', blank=True, null=True)

    def __str__(self):
        return str(self.nome) #+ ' - ' + str(self.cpf)


class Exame(models.Model):
    ESTADO = EstadosBrasileiros.estado_brasileiro
    nome_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo_exame = models.ForeignKey(TipoExame, on_delete=models.CASCADE)
    #nome_exame = models.ForeignKey(NomeExame, on_delete=models.CASCADE)
    data_exame = models.DateTimeField(auto_now=False, auto_now_add=False)
    data_exame_devolucao = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    exames_padrao = models.TextField(blank=True, null=True, help_text=("Notas sobre o paciente"))
    lista_exames = models.TextField(blank=True, null=True, help_text=("Exames ecolhidos par ao paciente"))
    obs_exame = models.TextField(blank=True, null=True, help_text=("Notas sobre o paciente"))

    def __str__(self):
        return str(self.nome_paciente) + ' - ' + str(self.tipo_exame)
