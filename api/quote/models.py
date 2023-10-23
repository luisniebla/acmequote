from django.db import models
from django.utils.translation import gettext_lazy as _


class Coverage(models.Model):
    name = models.CharField(max_length=200)
    monthly_price = models.DecimalField(decimal_places=2, max_digits=10)
    surcharge_fee = models.DecimalField(
        decimal_places=4, max_digits=5, null=True, blank=True
    )
    area = models.ForeignKey(
        'State',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class CoverageSurcharge(models.Model):
    coverage = models.ForeignKey('Coverage', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    fee = models.DecimalField(decimal_places=4, max_digits=5, null=True, blank=True)

    def __str__(self):
        return f'{self.coverage.name} - {self.state.name}'


class State(models.Model):
    name = models.CharField(max_length=200)
    tax = models.DecimalField(decimal_places=4, max_digits=5)

    def __str__(self):
        return self.name


class Quote(models.Model):
    class CovereageType(models.TextChoices):
        BASIC = "BS", _("Basic")
        PREMIUM = "PR", _("Premium")

    name = models.CharField(max_length=200)
    coverage_type = models.CharField(max_length=2, choices=CovereageType.choices)
    state = models.ForeignKey(
        'State',
        on_delete=models.CASCADE,
    )
    coverages = models.ManyToManyField(Coverage)

    def __str__(self):
        return self.name
