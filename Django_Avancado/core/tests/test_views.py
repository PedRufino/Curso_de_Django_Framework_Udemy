from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    
    def setUp(self) -> None:
        self.dados = {
            'nome': 'Pedro Neto',
            'email': 'pedro@test.com',
            'assunto': 'seila meu todo dia isso',
            'mensagem': 'de novo me deixa em paz kkkkkkkkkkkkk'
        }
        self.cliente = Client()
    
    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302)
    
    def test_form_invalid(self):
        dados = {
            'nome': 'Pedro Neto',
            'email': 'pedro@test.com',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200)