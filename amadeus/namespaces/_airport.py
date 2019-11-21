from amadeus.client.decorator import Decorator
from amadeus.airport._predictions import Predictions


class Airport(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.predictions = Predictions(client)
