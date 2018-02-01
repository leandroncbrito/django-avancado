import django
from django.urls import reverse

django.setup()

from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User

# Create your tests here.
"""SimpleTestCase não usa banco de dados, é uma implementação mais simples usada para test de unidade"""
"""TestCase testa a funcionalidade"""
from stock.models import Product, TimestampableMixin, StockEntry


class ProductTest(SimpleTestCase):
    def test_value_initial_stock_field(self):
        product = Product()
        self.assertEqual(0, product.stock)

    def test_product_has_timestampable(self):
        product = Product()
        self.assertIsInstance(product, TimestampableMixin)

    def test_exception_when_stock_less_zero(self):
        product = Product()
        with self.assertRaises(ValueError) as err:
            product.stock = 10
            product.decrement(11)
        self.assertEqual('Sem estoque disponível', str(err.exception))


class ProductDatabaseTest(TestCase):
    fixtures = ['data.json']

    # Escopo inicial
    def setUp(self):
        self.product = Product.objects.create(
            name="Produto",
            stock_max="200",
            price_sale=50,
            price_purchase=30
        )

    def test_product_save(self):
        self.assertEqual('Produto', self.product.name)
        self.assertEqual(self.product.stock, 0)

    def test_if_user_exists(self):
        user = User.objects.all().first()
        self.assertIsNotNone(user)


class StockEntryHttpTest(TestCase):
    fixtures = ['data.json']

    def setUp(self):
        self.product = Product.objects.create(
            name="Produto",
            stock_max="200",
            price_sale=50,
            price_purchase=30
        )

    def test_list(self):
        response = self.client.get('/stock/entries/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Produto Y', str(response.content))

    def test_create_a_new_entry(self):
        url = reverse('entries_create')
        self.product.stock = 100
        self.product.save()
        self.client.post(url, {'product': self.product.id, 'amount': 100})
        entry = StockEntry.objects.last()

        self.assertIsNotNone(entry)
        self.assertEqual(200, entry.product.stock)
