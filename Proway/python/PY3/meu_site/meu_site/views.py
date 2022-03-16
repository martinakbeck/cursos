from django.shortcuts import render
from cliente.models import Cliente, TpPessoa, UF, Cidade
from produto.models import Produto, Servico, Categoria

def lista_cursos(request):
    cursos = ['Python', 'HTML', 'CSS', 'JavaScript']
    linhas = len(cursos)
    return render(request, 'cursos.html', {'cursos' : cursos, 'total' : linhas})

def home(request):
    return render(request, 'inicio.html')


def lista_produtos(request):
    produto = Produto.objects.all().order_by('nome')
    totalProduto = produto.count()
    return render(request, 'lista-produtos.html', {'produto' : produto, 'total' : totalProduto})

def cadastrar_produto(request):
    categorias = Categoria.objects.all().order_by('nome')
    return render(request, 'cadastrar-produto.html', {'categoria' : categorias})

def altera_produto(request, id):
    return render(request, 'alterar-produto.html')

def excluir_produto(request, id):
    return render(request, 'excluir-produto.html')


def lista_categorias(request):
    categoria = Categoria.objects.all().order_by('nome')
    totalCategoria = categoria.count()
    return render(request, 'lista-categorias.html', {'categoria' : categoria, 'total' : totalCategoria})

def cadastrar_categoria(request):
    return render(request, 'cadastrar-categoria.html')

def altera_categoria(request, id):
    return render(request, 'alterar-categoria.html')

def excluir_categoria(request, id):
    return render(request, 'excluir-categoria.html')    


def lista_clientes(request):
    cliente = Cliente.objects.all().order_by('nome')
    totalCliente = cliente.count()
    return render(request, 'lista-clientes.html',{'cliente' : cliente, 'total' : totalCliente})

def cadastrar_cliente(request):
    cidade = Cidade.objects.all().order_by('nome')
    return render(request, 'cadastrar-cliente.html', {'cidade' : cidade})

def altera_cliente(request, id):
    return render(request, 'alterar-cliente.html')

def excluir_cliente(request, id):
    return render(request, 'excluir-produto.html')


def lista_tp_pessoas(request):
    tipo = TpPessoa.objects.all().order_by('nome')
    totalTipo = tipo.count()
    return render(request, 'lista-tp-pessoas.html', {'tipo' : tipo, 'total' : totalTipo})

def cadastrar_tp_pessoa(request):
    return render(request, 'cadastrar-tp-pessoa.html')

def altera_tp_pessoa(request, id):
    return render(request, 'alterar-tp-pessoa.html')

def excluir_tp_pessoa(request, id):
    return render(request, 'excluir-produto.html')


def lista_ufs(request):
    uf = UF.objects.all().order_by('nome')
    totalUF = uf.count()
    return render(request, 'lista-ufs.html', {'uf' : uf, 'total' : totalUF})

def cadastrar_uf(request):
    return render(request, 'cadastrar-uf.html')

def altera_uf(request, id):
    return render(request, 'alterar-uf.html')

def excluir_uf(request, id):
    return render(request, 'excluir-produto.html')


def lista_cidades(request):
    cidade = Cidade.objects.all().order_by('nome')
    totalCidade = cidade.count()
    return render(request, 'lista-cidades.html', {'cidade' : cidade, 'total' : totalCidade})

def cadastrar_cidade(request):
    uf = UF.objects.all().order_by('nome')
    return render(request, 'cadastrar-cidade.html', {'uf' : uf})

def altera_cidade(request, id):
    return render(request, 'alterar-cidade.html')

def excluir_cidade(request, id):
    return render(request, 'excluir-produto.html')


def lista_servicos(request):
    servico = Servico.objects.all().order_by('nome')
    totalServico = servico.count()
    return render(request, 'lista-servicos.html', {'servico' : servico, 'total' : totalServico})

def cadastrar_servico(request):
    return render(request, 'cadastrar-servico.html')

def altera_servico(request, id):
    return render(request, 'alterar-cidade.html')

def excluir_servico(request, id):
    return render(request, 'excluir-produto.html')

