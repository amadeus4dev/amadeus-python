from amadeus.client.decorator import Decorator


class HotelOffersSearch(Decorator, object):
    def get(self, **params):
        '''
        Get all offers given hotels

        .. code-block:: python

           amadeus.shopping.hotel_offers_search.get(hotelIds=RTPAR001',
            adults='2')

        :param hotelId: Amadeus Property Code (8 chars), for
            example ``RTPAR001``.

        :param adults: the number of adult passengers with age 12 or older

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v3/shopping/hotel-offers', **params)
