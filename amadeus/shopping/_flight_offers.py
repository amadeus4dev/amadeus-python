from amadeus.client.decorator import Decorator
from amadeus.shopping.flight_offers._prediction import FlightChoicePrediction
from amadeus.shopping.flight_offers._pricing import FlightOffersPrice
from amadeus.shopping.flight_offers._upselling import Upselling


class FlightOffers(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.prediction = FlightChoicePrediction(client)
        self.pricing = FlightOffersPrice(client)
        self.upselling = Upselling(client)
