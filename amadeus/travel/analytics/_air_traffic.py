from amadeus.client.decorator import Decorator
from .air_traffic._traveled import Traveled
from .air_traffic._booked import Booked
from .air_traffic._busiest_period import BusiestPeriod


class AirTraffic(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.booked = Booked(client)
        self.traveled = Traveled(client)
        self.busiest_period = BusiestPeriod(client)
