from amadeus.client.decorator import Decorator
from amadeus.shopping._flight_dates import FlightDates
from amadeus.shopping._flight_destinations import FlightDestinations
from amadeus.shopping._flight_offers import FlightOffers
from amadeus.shopping._flight_offers_search import FlightOffersSearch
from amadeus.shopping._seatmaps import Seatmaps
from amadeus.shopping._activities import Activities
from amadeus.shopping._activity import Activity
from amadeus.shopping._availability import Availability
from amadeus.shopping._hotel_offer_search import HotelOfferSearch
from amadeus.shopping._hotel_offers_search import HotelOffersSearch
from amadeus.shopping._transfer_offers import TransferOffers


class Shopping(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_dates = FlightDates(client)
        self.flight_destinations = FlightDestinations(client)
        self.flight_offers = FlightOffers(client)
        self.flight_offers_search = FlightOffersSearch(client)
        self.seatmaps = Seatmaps(client)
        self.activities = Activities(client)
        self.availability = Availability(client)
        self.hotel_offers_search = HotelOffersSearch(client)
        self.transfer_offers = TransferOffers(client)

    def hotel_offer_search(self, offer_id):
        return HotelOfferSearch(self.client, offer_id)

    def activity(self, activity_id):
        return Activity(self.client, activity_id)


__all__ = ['FlightDates', 'FlightDestinations', 'FlightOffers',
           'FlightOffersSearch', 'Availability']
