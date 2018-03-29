from amadeus.client.decorator import Decorator


class HotelOffers(Decorator, object):
    def get(self, **params):
        return self.client.get('/v1/shopping/hotel-offers', **params)
