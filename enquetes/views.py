from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Pergunta, Alternativa
# Create your views here.


class IndexView (View):
    def get(self, request, *args, **kwargs):
        lista = Pergunta.objects.all()
        context = {'lista_enquetes': lista}
        return render(request,"index.html", context)


class DetalhesView(View):
    template = "detalhes.html"

    def resposta(self, request, pergunta, error):
        contexto = {'enquete': pergunta, 'error': error}
        return render(request, self.template, contexto)

    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        return self.resposta(request, pergunta, None)


    def post(self, request, *args, **kwargs): # nova versão view de votação
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)

        try:
            alternativa_id = request.POST.get('alt')
            alternativa = pergunta.alternativa_set.get(pk=alternativa_id)
        except (KeyError, Alternativa.DoesNotExist):
            error =  "Você não selecionou nenhuma alternativa"
            return self.resposta(self, request, pergunta, error)
        else:
            alternativa.quant_votos += 1
            alternativa.save()

        return HttpResponseRedirect(reverse("resultados", kwargs={'pk': pergunta.id}))


class ResultadosView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id = kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        contexto =  {'enquete':pergunta}
        return render(request, "resultados.html", contexto)




# def resultados(request, pergunta_id):
#     pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
#     return render(request, "resultados.html", {'enquete': pergunta})


## Histórico de versões


# def index (request):
#     lista = Pergunta.objects.all()
#     context = {'lista_enquetes': lista}
#     return render(request,"index.html", context)

# class Myview(View):
# # parametros passados pela URL posso recuperar pela *args

# # **kwargs recupera chaves para o elemento de view

#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello word')

# # dispath -> resposta de um elemento de view


## View VOTACAO --> versão 1
# def votacao(request, pergunta_id):
#     pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
#     try:
#         alternativa_id = request.POST.get('alt')
#         alternativa = pergunta.alternativa_set.get(pk=alternativa_id)
#     except (KeyError, Alternativa.DoesNotExist):
#         context = {
#             'enquete': pergunta,
#             'error': "Você não selecionou nenhuma alternativa"
#         }
#         return render(request, "detalhes.html", context)
#     else:
#         alternativa.quant_votos += 1
#         alternativa.save()

#     return HttpResponseRedirect(reverse("resultados", args=(pergunta.id,)))

# View de DETALHES--> versão 1

# def detalhes(request, pergunta_id):
#     try:
#         enquete = Pergunta.objects.get(pk=pergunta_id);

#     except  Pergunta.DoesNotExist:
#         raise Http404("Questão não existe")

#     return render(request, "detalhes.html", {'enquete' :  enquete });
