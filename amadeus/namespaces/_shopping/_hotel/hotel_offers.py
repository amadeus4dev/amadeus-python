from amadeus.client.decorator import Decorator


class HotelOffers(Decorator, object):
    def __init__(self, client, hotel_id):
        Decorator.__init__(self, client)
        self.hotel_id = hotel_id

    def get(self, **params):
        return self.client.get(
            '/v1/shopping/hotels/{0}/hotel-offers'.format(self.hotel_id),
            **params
        )
