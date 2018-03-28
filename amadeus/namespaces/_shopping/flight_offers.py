from amadeus.client.decorator import Decorator


class FlightOffers(Decorator, object):
    def get(self, **params):
        return self.client.get('/v1/shopping/flight-offers', **params)
