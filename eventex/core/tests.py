from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use template index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

