from amadeus.client.decorator import Decorator

from .hotel._hotel_offers import HotelOffers
from .hotel._offer import Offer


class Hotel(Decorator, object):
    def __init__(self, client, hotel_id):
        Decorator.__init__(self, client)
        self.hotel_id = hotel_id
        self.hotel_offers = HotelOffers(client, hotel_id)

    def offer(self, offer_id):
        return Offer(self.client, self.hotel_id, offer_id)
