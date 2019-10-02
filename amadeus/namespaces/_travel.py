from amadeus.client.decorator import Decorator
from amadeus.travel._analytics import Analytics
from amadeus.travel._predictions import Predictions


class Travel(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.analytics = Analytics(client)
        self.predictions = Predictions(client)
