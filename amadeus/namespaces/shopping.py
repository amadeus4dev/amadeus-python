from amadeus.client.decorator import Decorator
from ._shopping.flight_dates import FlightDates
from ._shopping.flight_destinations import FlightDestinations
from ._shopping.flight_offers import FlightOffers


class Shopping(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_dates = FlightDates(client)
        self.flight_destinations = FlightDestinations(client)
        self.flight_offers = FlightOffers(client)
