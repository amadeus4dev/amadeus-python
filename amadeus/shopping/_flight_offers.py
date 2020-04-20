from amadeus.client.decorator import Decorator
from amadeus.shopping.flight_offers._prediction import FlightChoicePrediction
from amadeus.shopping.flight_offers._pricing import FlightOffersPrice


class FlightOffers(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.prediction = FlightChoicePrediction(client)
        self.pricing = FlightOffersPrice(client)
