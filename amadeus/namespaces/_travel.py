from amadeus.client.decorator import Decorator
from amadeus.travel._analytics import Analytics
from amadeus.travel._predictions import Predictions
from amadeus.travel._trip_parser_jobs import TripParser
from amadeus.travel._encoder import from_file, from_base64


class Travel(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.analytics = Analytics(client)
        self.predictions = Predictions(client)
        self.trip_parser_jobs = TripParser(client)

    def from_file(self, file):
        return from_file(file)

    def from_base64(self, base64):
        return from_base64(base64)
