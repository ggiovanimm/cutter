from django.urls import path
from .views import gerar_cutter, limpa_cutter


urlpatterns = [
    path('forms/', gerar_cutter, name='gerar_cutter'),  # Acessa o formulário na raiz
    path('limpa/', limpa_cutter, name='limpa_cutter'),  # Nome correto para limpar o formulário
]
