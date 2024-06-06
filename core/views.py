import asyncio
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .supabase_utils import _carrega_dados
#from .models import Movimentacao
import random


def home(request):
    return render(request, "index.html")

def redirect_to_core(request):
    return redirect('/core/')

def carregar_dados_view(request):
    _carrega_dados()
    return JsonResponse({'status': 'Dados carregados com sucesso'})

def inserir_coordenadas_aleatorias(request):
    # Gerar coordenadas aleatórias
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)

    # Inserir no banco de dados do Supabase
    movimentacao = movimentacao.objects.create(latitude=latitude, longitude=longitude)

    # Retornar uma resposta JSON indicando sucesso
    return JsonResponse({'status': 'success'})


