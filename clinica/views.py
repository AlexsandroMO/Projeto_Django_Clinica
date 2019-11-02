from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Paciente
from .models import Exame
from .forms import PacienteForm
from .forms import ExameForm
from django.contrib import messages
from django.core.paginator import Paginator
import prog



def home(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/home.html', {'pacientes': pacientes})


def listaPacientes(request):
    search = request.GET.get('search')
    if search:
        pacientes = Paciente.objects.filter(nome__icontains=search)
    else:
        paciente_list = Paciente.objects.all()
        paginator = Paginator(paciente_list, 4) #quantidde de linhas
        page = request.GET.get('page')
        pacientes = paginator.get_page(page)

    return render(request, 'clinica/lista-pacientes.html', {'pacientes': pacientes})#, 'cpf_number': cpf_number, 'cep_number': cep_number})


def listaView(request, id):
    pacientes = get_object_or_404(Paciente, pk=id)

    cpf = pacientes.cpf
    cpf_number = '{}.{}.{}-{}'.format(cpf[0:3],cpf[3:6], cpf[6:9],cpf[9:11])

    cep = pacientes.cep
    cep_number = '{}-{}'.format(cep[0:5],cep[5:8])

    return render(request, 'clinica/lista-view.html', {'pacientes': pacientes, 'cpf_number': cpf_number, 'cep_number': cep_number})


def newPaciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)

        if form.is_valid():
            pacientes = form.save(commit=False)
            pacientes.save()
            return redirect('/')

    else:
        form = PacienteForm()
        return render(request, 'clinica/addpaciente.html', {'form': form})


def editPaciente(request, id):
    pacientes = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(instance=pacientes)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=pacientes)

        if form.is_valid():
            pacientes.save()
            return redirect('/')
        else:
            return render(request, 'clinica/edit-paciente.html', {'form': form, 'pacientes': pacientes})

    else:
        return render(request, 'clinica/edit-paciente.html', {'form': form, 'pacientes': pacientes})


def deletePaciente(request, id):
    pacientes = get_object_or_404(Paciente, pk=id)
    pacientes.delete()

    messages.info(request, 'Paciente deletado com sucesso.')
    return redirect('/')


#================

def listaExames(request):
    search = request.GET.get('search')
    if search:
        exames = Exame.objects.filter(nome_paciente__icontains=search)
    else:
        exame_list = Exame.objects.all()
        paginator = Paginator(exame_list, 3) #quantidde de linhas
        page = request.GET.get('page')
        exames = paginator.get_page(page)

    return render(request, 'clinica/lista-exames.html', {'exames': exames})


def listaViewsExames(request, id):
    exames = get_object_or_404(Exame, pk=id)

    return render(request, 'clinica/lista-view-exame.html', {'exames': exames})


def editExame(request, id):
    exames = get_object_or_404(Exame, pk=id)
    form = ExameForm(instance=exames)

    if request.method == 'POST':
        form = ExameForm(request.POST, instance=exames)

        if form.is_valid():
            exames.save()
            return redirect('/')
        else:
            return render(request, 'clinica/edit-exame.html', {'form': form, 'exames': exames})

    else:
        return render(request, 'clinica/edit-exame.html', {'form': form, 'exames': exames})


def newExame(request):
    if request.method == 'POST':
        form = ExameForm(request.POST)

        if form.is_valid():
            exames = form.save(commit=False)
            exames.save()
            return redirect('url-lista-exames')

    else:
        form = ExameForm()
        return render(request, 'clinica/add-exame.html', {'form': form})


def deleteExame(request, id):
    exames = get_object_or_404(Exame, pk=id)
    exames.delete()

    messages.info(request, 'Exame deletado com sucesso.')
    return redirect('url-lista-exames')


def quadroExame(request):
    #print('Teste:')

    lista_df = prog.query_sql()
    df = lista_df[0]
    df = sorted(df)
    somatorio = lista_df[1]

    return render(request, 'clinica/quadro-exames.html', {'df': df, 'somatorio': somatorio})