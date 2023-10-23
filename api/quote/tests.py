from decimal import Decimal

from django.test import TestCase

from .models import Coverage, CoverageSurcharge, Quote, State
from .views import generate_price


class QuoteTestCase(TestCase):
    def setUp(self):
        ca = State.objects.create(name='CA', tax=0.01)
        tx = State.objects.create(name='TX', tax=0.005)
        ny = State.objects.create(name='NY', tax=0.02)
        Coverage.objects.create(name='Basic', monthly_price=20)
        Coverage.objects.create(name='Premium', monthly_price=40)
        Coverage.objects.create(name='Pet', monthly_price=20)
        flood = Coverage.objects.create(name='Flood', monthly_price=0)
        CoverageSurcharge.objects.create(coverage=flood, state=ca, fee=0.02)
        CoverageSurcharge.objects.create(coverage=flood, state=tx, fee=0.50)
        CoverageSurcharge.objects.create(coverage=flood, state=ny, fee=0.10)

    def test_quote_1(self):
        quote = Quote.objects.create(
            name='John Doe', state=State.objects.get(name='CA')
        )
        quote.coverages.add(Coverage.objects.get(name='Basic'))
        quote.coverages.add(Coverage.objects.get(name='Pet'))
        quote.coverages.add(Coverage.objects.get(name='Flood'))
        prices = generate_price(quote)
        self.assertEqual(prices['subtotal'], Decimal('40.80'))
        self.assertEqual(prices['taxes'], Decimal('0.40'))
        self.assertEqual(prices['total'], Decimal('40.80'))

    def test_quote_2(self):
        quote = Quote.objects.create(
            name='John Doe', state=State.objects.get(name='CA')
        )
        quote.coverages.add(Coverage.objects.get(name='Premium'))
        quote.coverages.add(Coverage.objects.get(name='Pet'))
        quote.coverages.add(Coverage.objects.get(name='Flood'))
        prices = generate_price(quote)
        self.assertEqual(prices['subtotal'], Decimal('61.20'))
        self.assertEqual(prices['taxes'], Decimal('0.61'))
        self.assertEqual(prices['total'], Decimal('61.81'))

    def test_quote_3(self):
        quote = Quote.objects.create(
            name='John Doe', state=State.objects.get(name='NY')
        )
        quote.coverages.add(Coverage.objects.get(name='Premium'))
        quote.coverages.add(Coverage.objects.get(name='Pet'))
        prices = generate_price(quote)
        self.assertEqual(prices['subtotal'], Decimal('60.00'))
        self.assertEqual(prices['taxes'], Decimal('1.20'))
        self.assertEqual(prices['total'], Decimal('61.20'))

    def test_quote_4(self):
        quote = Quote.objects.create(
            name='John Doe', state=State.objects.get(name='TX')
        )
        quote.coverages.add(Coverage.objects.get(name='Basic'))
        quote.coverages.add(Coverage.objects.get(name='Flood'))
        prices = generate_price(quote)
        self.assertEqual(prices['subtotal'], Decimal('30.00'))
        self.assertEqual(prices['taxes'], Decimal('0.15'))
        self.assertEqual(prices['total'], Decimal('30.15'))
