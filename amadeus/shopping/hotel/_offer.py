from amadeus.client.decorator import Decorator


class Offer(Decorator, object):
    def __init__(self, client, hotel_id, offer_id):
        Decorator.__init__(self, client)
        self.hotel_id = hotel_id
        self.offer_id = offer_id

    def get(self, **params):
        return self.client.get(
            '/v1/shopping/hotels/{0}/offers/{1}'.format(
                self.hotel_id, self.offer_id
            ), **params)
