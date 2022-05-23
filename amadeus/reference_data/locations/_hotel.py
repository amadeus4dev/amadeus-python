from amadeus.client.decorator import Decorator


class Hotel(Decorator, object):
    def get(self, **params):
        '''
        Returns a list of hotels matching a given keyword.

        .. code-block:: python


            amadeus.reference_data.locations.hotel.get(
                keyword='PARI',
                subType=[Hotel.HOTEL_LEISURE, Hotel.HOTEL_GDS]
            )

        :param keyword: location query keyword.
            For example: ``PARI``
        :param subType: category of search.
            For example: ``[Hotel.HOTEL_LEISURE, Hotel.HOTEL_GDS]``

        :rtype: amadeus.Response
        :raises amadeus.ResponseError: if the request could not be completed
        '''
        return self.client.get(
            '/v1/reference-data/locations/hotel', **params)
