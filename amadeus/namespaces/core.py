from amadeus.namespaces._reference_data import ReferenceData
from amadeus.namespaces._travel import Travel
from amadeus.namespaces._shopping import Shopping
from amadeus.namespaces._e_reputation import EReputation
from amadeus.namespaces._airport import Airport
from amadeus.namespaces._booking import Booking
from amadeus.namespaces._schedule import Schedule
from amadeus.namespaces._analytics import Analytics
from amadeus.namespaces._location import Location
from amadeus.namespaces._airline import Airline
from amadeus.namespaces._ordering import Ordering


class Core(object):
    def __init__(self):
        self.reference_data = ReferenceData(self)
        self.travel = Travel(self)
        self.shopping = Shopping(self)
        self.e_reputation = EReputation(self)
        self.airport = Airport(self)
        self.booking = Booking(self)
        self.schedule = Schedule(self)
        self.analytics = Analytics(self)
        self.location = Location(self)
        self.airline = Airline(self)
        self.ordering = Ordering(self)
