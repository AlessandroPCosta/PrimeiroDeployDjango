from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Produto

from django.http import HttpResponse
from django.template import loader

def index (request):
    #'Context' aparece la no index.html com  {{}}, duplas com a chave dentro, chamando a chave do dicionario

    # Descobrindo funcoes do request:
    #     print(dir(request))
    produtos = Produto.objects.all()
    context = {
        'curso' : 'Programação web com django frameworks',
        'outro' : 'Django é massa!',
        'produtos' : produtos
    }
    return render(request, 'index.html', context)

def contato (request):
    return render(request, 'contato.html')

def produto(resquest, pk):
    print(f'{pk}')
    # Importe essa parte da funcao, pois o mesmo nao é interavel, necessitando fazer a busca pelo id do objeto.
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto' : prod
    }
    return render(resquest, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html, charset=utf8', status=500)