from amadeus.client.decorator import Decorator
from amadeus.shopping._flight_dates import FlightDates
from amadeus.shopping._flight_destinations import FlightDestinations
from amadeus.shopping._flight_offers import FlightOffers
from amadeus.shopping._flight_offers_search import FlightOffersSearch
from amadeus.shopping._hotel_offers import HotelOffers
from amadeus.shopping._hotel_offers_by_hotel import HotelOffersByHotel
from amadeus.shopping._hotel_offer import HotelOffer
from amadeus.shopping._seatmaps import Seatmaps


class Shopping(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_dates = FlightDates(client)
        self.flight_destinations = FlightDestinations(client)
        self.flight_offers = FlightOffers(client)
        self.hotel_offers = HotelOffers(client)
        self.hotel_offers_by_hotel = HotelOffersByHotel(client)
        self.flight_offers_search = FlightOffersSearch(client)
        self.seatmaps = Seatmaps(client)

    def hotel_offer(self, offer_id):
        return HotelOffer(self.client, offer_id)


__all__ = ['FlightDates', 'FlightDestinations', 'FlightOffers',
           'FlightOffersSearch']
