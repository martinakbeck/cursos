from re import search
from django.contrib import admin
from .models import TpPessoa, CPFCNPJ, UF, Cidade, Cliente

# Register your models here.
class VisualizaCliente(admin.ModelAdmin):
    list_display = ['id','nome', 'cpfcnpj', 'estado_civil']
    list_display_links = ['id', 'nome']
    list_per_page = 5
    search_fields = ['nome', 'email']
    fieldsets = [
        ('Dados básico',{'fields':('nome', 'cpfcnpj', 'sexo','nasc', 'cidade')}),
        ('Complementares',{'fields':('filhos', 'carro','estado_civil')}),
        ('Financeiro',{'fields':('profissao', 'renda')}),


    ]
    #fields = ['nome', 'email']
    #list_filter = ['nome', 'email']



admin.site.register(TpPessoa)
admin.site.register(CPFCNPJ)
admin.site.register(Cliente, VisualizaCliente)
admin.site.register(UF)
admin.site.register(Cidade)
