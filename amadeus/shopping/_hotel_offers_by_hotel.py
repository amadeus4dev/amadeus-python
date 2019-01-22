from amadeus.client.decorator import Decorator


class HotelOffersByHotel(Decorator, object):
    def get(self, **params):
        '''
        Get all offers for Holiday Inn Paris Notre Dame.

        .. code-block:: python

            amadeus.shopping.hotel_offers_by_hotel.get(hotelId='XKPARC12')

        :param hotelId: Amadeus Property Code (8 chars), for
            example ``XKPARC12``.

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v2/shopping/hotel-offers/by-hotel', **params)
