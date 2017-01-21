from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Rodrigo Lima',
            cpf='06122351903',
            email='contato@homebrewbrasil.com.br',
            phone='11972133986'
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Rodrigo Lima', str(self.obj))