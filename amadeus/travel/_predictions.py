from amadeus.client.decorator import Decorator
from .predictions import TripPurpose


class Predictions(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.trip_purpose = TripPurpose(client)
