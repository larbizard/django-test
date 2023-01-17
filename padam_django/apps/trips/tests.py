from django.test import TestCase
from .models import BusShift, BusStop
from padam_django.apps.geography.models import Place
from padam_django.apps.fleet.models import Driver, Bus
from padam_django.apps.users.models import User

class TestTrips(TestCase):

    def testBusStopCreation(self):
        place1 = Place.objects.create(name="Test place", longitude="23.5", latitude="7.1")
        bustop = BusStop.objects.create(place=place1, arrival_time='09:00', departure_time='09:01')

        assert place1 == bustop.place

    def testBusShiftCreation(self):
        user = User.objects.create(username='Dupont', email='dupont@webmail.com', password='Acouteauxtires')
        driver = Driver.objects.create(user=user)
        bus = Bus.objects.create(licence_plate="A1A1-WW-ZZ")
        place1 = Place.objects.create(name="Test place 1", longitude="23.5", latitude="7.1")
        place2 = Place.objects.create(name="Test place 2", longitude="23.0", latitude="6.9")
        bustop1 = BusStop.objects.create(place=place1, arrival_time='09:00', departure_time='09:01')
        bustop2 = BusStop.objects.create(place=place2, arrival_time='10:00', departure_time='10:01')

        bus_shift = BusShift.objects.create(bus=bus, driver=driver)

        bus_shift.stops.add(bustop1)
        bus_shift.stops.add(bustop2)

        assert driver == bus_shift.driver