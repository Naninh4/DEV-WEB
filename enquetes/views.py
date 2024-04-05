from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Pergunta, Alternativa
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
    try:
        enquete = Pergunta.objects.get(pk=pergunta_id);

    except  Pergunta.DoesNotExist:
        raise Http404("Questão não existe")

    return render(request, "detalhes.html", {'enquete' :  enquete });


def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        alternativa_id = request.POST.get('alt')
        alternativa = pergunta.alternativa_set.get(pk=alternativa_id)
    except (KeyError, Alternativa.DoesNotExist):
        context = {
            'enquete': pergunta,
            'error': "Você não selecionou nenhuma alternativa"
        }
        return render(request, "detalhes.html", context)
    else:
        alternativa.quant_votos += 1
        alternativa.save()

    return HttpResponseRedirect(reverse("resultados", args=(pergunta.id,)))

def resultados(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "resultados.html", {'enquete': pergunta})