from amadeus_sdk.client.decorator import Decorator
from amadeus_sdk.shopping._flight_dates import FlightDates
from amadeus_sdk.shopping._flight_destinations import FlightDestinations
from amadeus_sdk.shopping._flight_offers import FlightOffers
from amadeus_sdk.shopping._hotel_offers import HotelOffers
from amadeus_sdk.shopping._hotel import Hotel


class Shopping(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_dates = FlightDates(client)
        self.flight_destinations = FlightDestinations(client)
        self.flight_offers = FlightOffers(client)
        self.hotel_offers = HotelOffers(client)

    def hotel(self, hotel_id):
        return Hotel(self.client, hotel_id)


__all__ = ['FlightDates', 'FlightDestinations', 'FlightOffers']
