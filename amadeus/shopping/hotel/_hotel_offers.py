from amadeus.client.decorator import Decorator


class HotelOffers(Decorator, object):
    def __init__(self, client, hotel_id):
        Decorator.__init__(self, client)
        self.hotel_id = hotel_id

    def get(self, **params):
        '''
        Get available offers for a specific hotel

        .. code-block:: python

            amadeus.shopping.hotel('SMPARCOL').hotel_offers.get()

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/shopping/hotels/{0}/hotel-offers'.format(self.hotel_id),
            **params
        )
