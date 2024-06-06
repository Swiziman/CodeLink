from django.contrib import admin
from django.urls import path, include
from .views import home, carregar_dados_view


urlpatterns = [
   path('', home),
   path('carregar-dados/', carregar_dados_view, name='carregar_dados'),
   
]
