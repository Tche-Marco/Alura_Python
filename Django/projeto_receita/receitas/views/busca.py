from receitas.models import Receita
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


def buscar(request):
    lista_receitas = Receita.objects.order_by(
        '-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        lista_receitas = lista_receitas.filter(
            nome_receita__icontains=nome_a_buscar)

    return render(request, 'receitas/buscar.html', {'receitas': lista_receitas})