from django import forms
from django.contrib import admin
from .models import BusShift, BusStop
from django.core.exceptions import ValidationError


class BusShiftForm(forms.ModelForm):

    def clean(self, *args, **kwargs):

        if 'stops' not in self.cleaned_data or len(self.cleaned_data['stops']) < 2:
            raise ValidationError({"stops": "There must be at least two stops"})

        busshifts = BusShift.objects.all()

        for bush_shift in busshifts:

            stops = BusStop.objects.filter(shiftstops__id=bush_shift.pk)

            if bush_shift.bus.pk == self.cleaned_data['bus'].pk:
                if (stops.first().departure_time <= self.cleaned_data['stops'].first().departure_time and stops.last().departure_time >= self.cleaned_data['stops'].last().arrival_time) or (stops.first().departure_time >= self.cleaned_data['stops'].last().arrival_time and stops.last().departure_time <= self.cleaned_data['stops'].last().arrival_time):
                    raise ValidationError({"bus": "A bus cannot be used at the same time on both Bus Shifts"})

            if bush_shift.driver.pk == self.cleaned_data['driver'].pk:
                if (stops.first().departure_time <= self.cleaned_data['stops'].first().departure_time and stops.last().departure_time >= self.cleaned_data['stops'].last().arrival_time) or (stops.first().departure_time >= self.cleaned_data['stops'].last().arrival_time and stops.last().departure_time <= self.cleaned_data['stops'].last().arrival_time):
                    raise ValidationError({"bus": "A driver cannot be on two shifts at same time"})

        return super(BusShiftForm, self).clean(*args, **kwargs)