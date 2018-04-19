from amadeus.client.decorator import Decorator
from .analytics.air_traffic._traveled import Traveled
from .analytics._fare_searches import FareSearches


class Analytics(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.traveled = Traveled(client)
        self.fare_searches = FareSearches(client)
