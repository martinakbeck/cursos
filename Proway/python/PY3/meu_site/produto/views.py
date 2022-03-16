from django.shortcuts import render

# Create your views here.

def lista_produto(request):
    return render(request, 'lista-produtos.html')