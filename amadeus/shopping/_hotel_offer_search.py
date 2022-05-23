from amadeus.client.decorator import Decorator


class HotelOfferSearch(Decorator, object):
    def __init__(self, client, offer_id):
        Decorator.__init__(self, client)
        self.offer_id = offer_id

    def get(self, **params):
        '''
        Returns details for a specific offer

        .. code-block:: python

            amadeus.shopping.hotel_offer_search('XXX').get

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v3/shopping/hotel-offers/{0}'
                               .format(self.offer_id), **params)
