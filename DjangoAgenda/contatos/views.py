from django.shortcuts import render, get_object_or_404
from .models import Contato
from .forms import FormularioCadstro


# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})


def amigos(request):
    contatos = Contato.objects.all().filter(categoria='3')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})


def familia(request):
    contatos = Contato.objects.all().filter(categoria='1')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})


def empresa(request):
    contatos = Contato.objects.all().filter(categoria='2')
    return render(request, 'contatos/index.html',
                  {'contatos': contatos})


def exibir_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    return render(request, 'contatos/exibir_contato.html', {
        'contato': contato
    })


def cadastrar_contato(request):
    if request.method == 'GET':
        form = FormularioCadstro()
        return render(request, 'contatos/cadastrar_contato.html', {'form': form})
    else:
        form = FormularioCadstro(request.POST)
        if form.is_valid():
            cadastro = form.save()
            form = FormularioCadstro()
            return index(request)
        else:
            return render(request, "contatos/cadastrar_contato.html",
                          {'form': form})
