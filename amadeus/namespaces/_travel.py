from amadeus.client.decorator import Decorator
from amadeus.travel._analytics import Analytics
from amadeus.travel._predictions import Predictions
from amadeus.travel._trip_parser import TripParser
from amadeus.travel._encoder import from_file, from_base64


class Travel(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.analytics = Analytics(client)
        self.predictions = Predictions(client)
        self.trip_parser = TripParser(client)

    @staticmethod
    def from_file(file):
        return from_file(file)

    @staticmethod
    def from_base64(base64):
        return from_base64(base64)
