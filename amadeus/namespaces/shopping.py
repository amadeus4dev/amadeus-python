from amadeus.client.decorator import Decorator
from ._shopping.flight_dates import FlightDates
from ._shopping.flight_destinations import FlightDestinations
from ._shopping.flight_offers import FlightOffers
from ._shopping.hotel_offers import HotelOffers
from ._shopping.hotel import Hotel


class Shopping(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_dates = FlightDates(client)
        self.flight_destinations = FlightDestinations(client)
        self.flight_offers = FlightOffers(client)
        self.hotel_offers = HotelOffers(client)

    def hotel(self, hotel_id):
        return Hotel(self.client, hotel_id)
