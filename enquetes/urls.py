from django.urls import path
from .views import index, votacao, detalhes, resultados

urlpatterns = [
    path('', index, name="index"),
    path('<int:pergunta_id>/votacao',votacao, name='votacao' ),
    path('<int:pergunta_id>/detalhes', detalhes, name="detalhes"),
    path('<int:pergunta_id>/resultado', resultados, name="resultados"),
]