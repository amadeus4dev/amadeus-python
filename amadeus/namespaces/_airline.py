from amadeus.client.decorator import Decorator
from amadeus.airline._destinations import Destinations


class Airline(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.destinations = Destinations(client)
