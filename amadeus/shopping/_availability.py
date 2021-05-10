from amadeus.client.decorator import Decorator
from .availability import FlightAvailabilities


class Availability(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_availabilities = FlightAvailabilities(client)
