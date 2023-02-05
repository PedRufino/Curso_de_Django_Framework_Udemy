from django.contrib import admin

# Register your models here.

from .models import Produto, Cliente

# Cria uma tabela com nome, preço e estoque no Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque')

# Cria uma tabela com nome, sobrenome e email no Cliente
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')

# admin.site.register(Produto) -> traz o banco de dados (Produto) na area de admin
# admin.site.register(Produto,ProdutoAdmin) -> Adicionando (ProdutoAdmin) cria uma tabela
# com informações escolhidas no (class)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)