from amadeus.client.decorator import Decorator


class FlightDestinations(Decorator, object):
    def get(self, **params):
        return self.client.get('/v1/shopping/flight-destinations', **params)
