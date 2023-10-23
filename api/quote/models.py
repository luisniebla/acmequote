import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Coverage(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    monthly_price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class CoverageSurcharge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coverage = models.ForeignKey('Coverage', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    fee = models.DecimalField(decimal_places=4, max_digits=5, null=True, blank=True)

    def __str__(self):
        return f'{self.coverage.name} - {self.state.name}'


class State(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    tax = models.DecimalField(decimal_places=4, max_digits=5)

    def __str__(self):
        return self.name


class Quote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    state = models.ForeignKey(
        'State',
        on_delete=models.CASCADE,
    )
    coverages = models.ManyToManyField(Coverage)

    def __str__(self):
        return self.name
