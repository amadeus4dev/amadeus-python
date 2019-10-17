from amadeus.client.decorator import Decorator
from amadeus.e_reputation._hotel_sentiments import HotelSentiments


class EReputation(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.hotel_sentiments = HotelSentiments(client)
