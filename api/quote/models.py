from django.db import models
from django.utils.translation import gettext_lazy as _


class Coverage(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=4, max_digits=5)
    state_rates = models.ForeignKey('State', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
