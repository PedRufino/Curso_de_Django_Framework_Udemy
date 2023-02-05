from django.db import models

# Admin django
# Login: pedro
# senha: 152319

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=10)
    estoque = models.IntegerField('Quantidade em Estoque')
    
    # Para aparecer o nome do produto no admin 
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    celular = models.IntegerField('Celular')
    cpf = models.IntegerField('CPF')
    
    # Para aparecer o nome e sobrenome do cliente no admin 
    # ex: Cliente object (1) para Pedro Neto
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'