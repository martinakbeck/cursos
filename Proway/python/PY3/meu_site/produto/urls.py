from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import lista_produto

urlpaterns = [
    path('produto-lista', lista_produto),
]