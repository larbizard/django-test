from django.db import models

class BusShift(models.Model):

    bus = models.ForeignKey('fleet.Bus', on_delete=models.CASCADE, related_name='busshift')
    driver = models.ForeignKey('fleet.Driver', on_delete=models.CASCADE, related_name='shiftdriver')
    stops = models.ManyToManyField('trips.BusStop', related_name='shiftstops')

    def __str__(self) -> str:
        return super().__str__()

class BusStop(models.Model):
    place = models.OneToOneField('geography.Place', on_delete=models.CASCADE, related_name='stopplace')
    arrival_time = models.TimeField()
    departure_time = models.TimeField()

    def __str__(self) -> str:
        return super().__str__()