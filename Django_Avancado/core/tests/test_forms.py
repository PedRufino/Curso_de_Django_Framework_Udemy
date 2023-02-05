from django.test import TestCase
from core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self) -> None:
        self.nome = 'Pedro Neto'
        self.email = 'pedro@test.com'
        self.assunto = 'seila meu todo dia isso'
        self.mensagem = 'de novo me deixa em paz kkkkkkkkkkkkk'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }
        
        self.form = ContatoForm(data=self.dados) # ContatoForm(request.Post)

    def test_send_email(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()
        
        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()
        
        self.assertEquals(res1, res2)