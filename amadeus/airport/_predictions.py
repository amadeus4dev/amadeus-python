from amadeus.client.decorator import Decorator
from .predictions import AirportOnTime


class Predictions(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.on_time = AirportOnTime(client)
