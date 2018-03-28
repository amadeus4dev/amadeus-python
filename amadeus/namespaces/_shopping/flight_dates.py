from amadeus.client.decorator import Decorator


class FlightDates(Decorator, object):
    def get(self, **params):
        return self.client.get('/v1/shopping/flight-dates', **params)
