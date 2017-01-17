from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Rodrigo Lima", cpf="12345678901",
                    email="contato@homebrewbrasil.com.br", phone="11972133986")

        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@homebrewbrasil.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@homebrewbrasil.com.br', 'contato@homebrewbrasil.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_emai_body(self):
        contents = [
            'Rodrigo Lima',
            '12345678901',
            'contato@homebrewbrasil.com.br',
            '11972133986',
            'Rodrigo Lima',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

