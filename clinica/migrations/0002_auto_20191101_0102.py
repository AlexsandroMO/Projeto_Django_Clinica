# Generated by Django 2.2.6 on 2019-11-01 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='aniversario',
            field=models.DateField(verbose_name='ANIVERSÁRIO'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='bairro',
            field=models.CharField(max_length=100, verbose_name='BAIRRO'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cep',
            field=models.CharField(max_length=8, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cidade',
            field=models.CharField(max_length=100, verbose_name='CIDADE'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Cliente', verbose_name='EMPRESA'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='estado',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=60, verbose_name='ESTADO'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='FOTO'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Genero', verbose_name='GÊNERO'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nome',
            field=models.CharField(max_length=70, verbose_name='NOME'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='numero',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6, verbose_name='NÚMERO'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rua',
            field=models.IntegerField(max_length=100, verbose_name='RUA'),
        ),
    ]