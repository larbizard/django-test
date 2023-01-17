from django.contrib import admin

from . import models

from .forms import BusShiftForm


@admin.register(models.BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    form = BusShiftForm
    pass

@admin.register(models.BusStop)
class BusStopAdmin(admin.ModelAdmin):
    pass
