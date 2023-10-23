from django.contrib import admin

from .models import Coverage, CoverageSurcharge, Quote, State

# Register your models here.
admin.site.register(Quote)
admin.site.register(State)
admin.site.register(Coverage)
admin.site.register(CoverageSurcharge)
