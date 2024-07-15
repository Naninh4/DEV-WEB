from django.urls import path
from . import views
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>', views.DetalhesView.as_view(), name="detalhes"),
    path('<int:pk>/resultados', views.ResultadosView.as_view(), name="resultados"),
]

# path('<int:pk>/votacao',votacao, name='votacao' ), // não precisa mais :)