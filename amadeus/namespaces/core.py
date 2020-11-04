from amadeus.namespaces._reference_data import ReferenceData
from amadeus.namespaces._travel import Travel
from amadeus.namespaces._shopping import Shopping
from amadeus.namespaces._e_reputation import EReputation
from amadeus.namespaces._airport import Airport
from amadeus.namespaces._media import Media
from amadeus.namespaces._booking import Booking
from amadeus.namespaces._safety import Safety
from amadeus.namespaces._schedule import Schedule
from amadeus.namespaces._analytics import Analytics


class Core(object):
    def __init__(self):
        self.reference_data = ReferenceData(self)
        self.travel = Travel(self)
        self.shopping = Shopping(self)
        self.e_reputation = EReputation(self)
        self.airport = Airport(self)
        self.media = Media(self)
        self.booking = Booking(self)
        self.safety = Safety(self)
        self.schedule = Schedule(self)
        self.analytics = Analytics(self)
