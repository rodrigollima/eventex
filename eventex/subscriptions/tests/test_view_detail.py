from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetaiGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Rodrigo Lima',
            cpf='12345678901',
            email='contato@homebrewbrasil.com.br',
            phone='11972133986'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def teste_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        print(self.resp)
        self.assertEqual(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscriptin = self.resp.context['subscription']
        self.assertIsInstance(subscriptin, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)