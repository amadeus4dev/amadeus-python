from amadeus.client.decorator import Decorator
from .analytics._air_traffic import AirTraffic
from .analytics._fare_searches import FareSearches


class Analytics(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.air_traffic = AirTraffic(client)
        self.fare_searches = FareSearches(client)
