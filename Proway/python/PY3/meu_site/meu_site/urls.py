"""meu_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import home
from .views import lista_clientes, cadastrar_cliente, altera_cliente, excluir_cliente
from .views import lista_produtos, cadastrar_produto, altera_produto, excluir_produto
from .views import lista_cidades, cadastrar_cidade, altera_cidade, excluir_cidade
from .views import lista_tp_pessoas, cadastrar_tp_pessoa, altera_tp_pessoa, excluir_tp_pessoa
from .views import lista_ufs, cadastrar_uf, altera_uf, excluir_uf
from .views import lista_servicos, cadastrar_servico, altera_servico, excluir_servico
from .views import lista_categorias, cadastrar_categoria, altera_categoria, excluir_categoria
from produto import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home),
    
    path('lista-produto', lista_produtos),
    path('cadastro-produto', cadastrar_produto),
    path('altera-produto', altera_produto),
    path('exclui-produto', excluir_produto),

    path('lista-categoria', lista_categorias),
    path('cadastro-categoria', cadastrar_categoria),
    path('altera-categoria', altera_categoria),
    path('exclui-categoria', excluir_categoria),

    path('lista-cliente', lista_clientes),
    path('cadastro-cliente', cadastrar_cliente),
    path('altera-cliente', altera_cliente),
    path('exclui-cliente', excluir_cliente),

    path('lista-cidade', lista_cidades),
    path('cadastro-cidade', cadastrar_cidade),
    path('altera-cidade', altera_cidade),
    path('exclui-cidade', excluir_cidade),

    path('lista-tp-pessoa', lista_tp_pessoas),
    path('cadastro-tp-pessoa', cadastrar_tp_pessoa),
    path('altera-tp-pessoa', altera_tp_pessoa),
    path('exclui-tp-pessoa', excluir_tp_pessoa),

    path('lista-ufs', lista_ufs),
    path('cadastro-uf', cadastrar_uf),
    path('altera-uf', altera_uf),
    path('exclui-uf', excluir_uf),

    path('lista-servico', lista_servicos),
    path('cadastro-servico', cadastrar_servico),
    path('altera-servico', altera_servico),
    path('exclui-servico', excluir_servico),

    path('contato', TemplateView.as_view(template_name='contato.html')),
    path('login', TemplateView.as_view(template_name='login.html')),
    path('', home),
]
