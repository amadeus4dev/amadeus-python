from amadeus.client.decorator import Decorator
from amadeus.analytics._itinerary_price_metrics import ItineraryPriceMetrics


class Analytics(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.itinerary_price_metrics = ItineraryPriceMetrics(client)
