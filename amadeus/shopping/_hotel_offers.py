from amadeus.client.decorator import Decorator


class HotelOffers(Decorator, object):
    def get(self, **params):
        '''
        Search for hotels and retrieve availability and rates information.

        Use either `cityCode`, `longitude` and `latitude` or `hotelIds` to
        make a search.

        .. code-block:: python

            amadeus.shopping.hotel_offers.get(cityCode='PAR')
            amadeus.shopping.hotel_offers.get(longitude=49.0, latitude=2.0)
            amadeus.shopping.hotel_offers.get(hotelIds='RTPAR001, RTPAR002')

        :param cityCode: the City IATA code for which to find a hotel, for
            example ``"BOS"`` for Boston.
        :param latitude: latitude of geographic location to search around.
            For example: ``52.5238``
        :param longitude: longitude of geographic location to search around.
            For example: ``13.3835``
        :param hotelIds: Comma separated list of Amadeus hotel codes to request.
            Example: ``RTPAR001``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get('/v2/shopping/hotel-offers', **params)
