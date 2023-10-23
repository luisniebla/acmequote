from decimal import Decimal

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import CoverageSurcharge, Quote


def generate_price(quote):
    subtotal = 0
    for coverage in quote.coverages.all():
        subtotal += Decimal(coverage.monthly_price)

    surcharges = CoverageSurcharge.objects.filter(
        coverage__in=quote.coverages.all(),
        state=quote.state,
    )

    for surcharge in surcharges:
        subtotal = subtotal + subtotal * Decimal(surcharge.fee)

    tax = Decimal(quote.state.tax) * Decimal(subtotal)
    quant = lambda x: Decimal(x).quantize(Decimal('0.01'))
    return {
        'subtotal': quant(subtotal),
        'taxes': quant(tax),
        'total': quant(subtotal + tax),
    }


def index(request, resource_id):
    quote = get_object_or_404(Quote, pk=resource_id)
    # TODO: Should add non-nullable primary_coverage to Quote
    primary_coverage = (
        quote.coverages.filter(name='Basic').first()
        or quote.coverages.filter(name='Premium').first()
    )
    prices = generate_price(quote)
    return HttpResponse(
        f'''
        {quote.name}:
            Coverage Type: {primary_coverage.name}
            State: {quote.state}
            Has Pet: {quote.coverages.filter(name='Pet').exists()}
            Flood Coverage: {quote.coverages.filter(name='Flood').exists()}
            Price:
                Monthly Subtotal: ${prices['subtotal']}
                Monthly Taxes: ${prices['taxes']}
                Monthly Total: ${prices['total']}
        '''
    )
