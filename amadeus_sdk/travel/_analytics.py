from amadeus_sdk.client.decorator import Decorator
from .analytics._air_traffics import AirTraffics
from .analytics._fare_searches import FareSearches


class Analytics(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.air_traffics = AirTraffics(client)
        self.fare_searches = FareSearches(client)
