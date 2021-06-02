from amadeus.client.decorator import Decorator
from amadeus.location._analytics import Analytics


class Location(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.analytics = Analytics(client)
