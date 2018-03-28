from amadeus.client.decorator import Decorator
from ._locations.airports import Airports


class Locations(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.airports = Airports(client)

    def get(self, **params):
        return self.client.get('/v1/reference-data/locations', **params)
