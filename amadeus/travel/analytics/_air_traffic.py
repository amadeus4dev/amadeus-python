from amadeus.client.decorator import Decorator
from .air_traffic._traveled import Traveled
from .air_traffic._booked import Booked
from .air_traffic._searched import Searched
from .air_traffic._searched_by_destination import SearchedByDestination
from .air_traffic._busiest_period import BusiestPeriod


class AirTraffic(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.booked = Booked(client)
        self.traveled = Traveled(client)
        self.searched = Searched(client)
        self.searched_by_destination = SearchedByDestination(client)
        self.busiest_period = BusiestPeriod(client)
