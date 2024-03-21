from django.shortcuts import render
from django.http import  HttpResponse

from .models import Pergunta
# Create your views here.


# def index (request):
#     return


def index (request):
    lista = Pergunta.objects.all()
    context = {'lista_enquetes': lista}
    return render(request,"index.html", context)

# def index (request):
#     lista = Pergunta.objects.all()
#     template = loader.get_template('templates/index.html')
#     context = {'lista_enquetes': lista}
#     return HttpResponse(template.render(request, context))

def detalhes(request, pergunta_id):
    resultado = "<h1> Detalhes da enquete de número: %s </h1>"
    return HttpResponse( resultado % pergunta_id)

def votacao(request, pergunta_id):
    resultado = "<h1> Votacões da enquete de número: %s</h1> "
    return HttpResponse( resultado % pergunta_id)

def resultados(request, pergunta_id):
    resultado = "<h1> RESULTADOS enquete de número: %s </h1>"
    return HttpResponse(resultado % pergunta_id)