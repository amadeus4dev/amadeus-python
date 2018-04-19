from amadeus.client.decorator import Decorator
from .air_traffic._traveled import Traveled


class AirTraffic(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.traveled = Traveled(client)
