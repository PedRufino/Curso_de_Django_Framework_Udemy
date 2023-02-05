from math import prod
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Produto

def index(request):
    # print(dir(request.user))
    # print(f"User: {request.user}")
    produtos = Produto.objects.all()

    if str(request.user) == 'AnonymousUser':
        teste = 'Usuário não logado'
    else:
        teste = 'Usuário Logado'
        
    context = {
        'curso' : 'Programação Web com Django Framework',
        'Ped' : 'O Pedro esta aprendendo Django',
        'teste': teste,
        'produtos': produtos,
        
    }
    return render(request,'index.html', context)

def contato(request):
    return render(request,'contato.html')

def produto(request, pk):
    print(f'PK: {pk}')
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
# >>> produto.save()
# >>> produto = Produto(nome="NoteBook Acer", preco=4000.00, estoque=15)
