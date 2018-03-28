from amadeus.client.decorator import Decorator
from ._analytics.air_traffics import AirTraffics
from ._analytics.fare_searches import FareSearches


class Analytics(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.air_traffics = AirTraffics(client)
        self.fare_searches = FareSearches(client)
