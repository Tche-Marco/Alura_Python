from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita


def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    return render(request, 'index.html', {'receitas': receitas})


def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    return render(request, 'receita.html', {'receita': receita})


def buscar(request):
    lista_receitas = Receita.objects.order_by(
        '-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(
                nome_receita__icontains=nome_a_buscar)

    return render(request, 'buscar.html', {'receitas': lista_receitas})
